# -*- coding: utf-8 -*-
"""
optrace.raytrace
================

Classes and methods to simulate light-ray propagation.
"""

import sys
import multiprocessing as mp
import itertools as it
from time import time

import numpy as np
import scipy.optimize as so
import scipy.stats as st

from PyQt5 import QtCore, QtWidgets
import pyqtgraph.opengl as gl
from pyqtgraph.opengl.GLGraphicsItem import GLGraphicsItem

from qspec.qtypes import *
from qspec import tools
from qspec.physics import sellmeier


# TODO: Iterable first in constructor of list types.
def axis_equal_3d(ax):
    extents = np.array([getattr(ax, 'get_{}lim'.format(dim))() for dim in 'xyz'])
    sz = extents[:, 1] - extents[:, 0]
    centers = np.mean(extents, axis=1)
    maxsize = max(abs(sz))
    r = maxsize/2
    for ctr, dim in zip(centers, 'xyz'):
        getattr(ax, 'set_{}lim'.format(dim))(ctr - r, ctr + r)


def sphere_intersection(center, radius, origin, direction):
    oc = (origin - np.expand_dims(center, axis=0))
    discriminant = np.sum(direction * oc, axis=-1) ** 2 - (tools.absolute(oc, axis=-1) ** 2 - radius ** 2)
    ret = -np.sum(direction * oc, axis=-1)
    ret = [ret + np.sqrt(discriminant), ret - np.sqrt(discriminant)]
    nan = discriminant < 0.
    ret[0][nan] = np.nan
    ret[1][nan] = np.nan
    ret[0][~nan], ret[1][~nan] = np.min(ret), np.max(ret)
    return ret


def straight3d(t, r0, dr):
    if isinstance(t, float):
        return r0 + dr * t
    if r0.shape[0] != t.shape[0]:
        return np.expand_dims(r0, axis=0) + np.expand_dims(dr, axis=0) * np.expand_dims(t, axis=-1)
    return r0 + dr * np.expand_dims(t, axis=-1)


class Visualizer3D(object):
    """
    A 3d-visualizer of the ray-tracing scene using OpenGL. OpenGL PlotItems can be added with 'add_item()'.
    The scene can be displayed with the 'show()' method. 
    """
    def __init__(self, label: str):
        """
        :param label: The label of the Visualizer3D object.
        """
        self.label = label
        self.app = QtWidgets.QApplication(sys.argv)
        self.w = gl.GLViewWidget()
        self.w.opts['distance'] = 100
        self.w.setWindowTitle(self.label)
        self.w.setGeometry(0, 110, 1920, 1080)

    def add_item(self, item: GLGraphicsItem):
        """
        :param item: The item to add.
        :returns: None. Adds an item to the scene.
        """
        self.w.addItem(item)

    def show(self):
        """
        :returns: None. Starts the GUI, showing the 3D scene.
        """
        self.w.show()
        if (sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
            self.app.exec_()


class Material(object):
    """
    Class representing a material. For lenses, a single index of refraction 'n' or alternatively,
     arbitrary many pairs of sellmeier 'coefficients' A (numerator) and B (denominator), which overrides 'n',
     can be defined. For mirrors, a dictionary with wavelengths (µm) as keys and reflection coefficients as values
     can be defined. The reflection coefficients for unspecified wavelengths are interpolated
     with a polynomial of maximum possible order.
    """
    def __init__(self, label: str = 'Vacuum', n: complexscalar = 1.,
                 coefficients: array_iter = None, reflections: dict = None):
        """
        :param label: The label of the material. Should be unique.
        :param n: The index of refraction, wavelength-independent.
        :param coefficients: Sellmeier coefficients A and B. 'coefficients' must have shape (2, n), n > 1.
        :param reflections: Reflection coefficients for different wavelengths.
         Missing wavelengths are interpolated with a polynomial of maximum possible order.
        """
        self.label = label
        self.n = complex(n)  # Used for lenses
        self.n_real = self.n.real
        self.n_imag = self.n.imag
        self.coefficients = coefficients  # Used for lenses, overrides 'self.n'
        self.reflections: Union[dict, None] = None
        self.p: Union[Callable, None] = None
        self.set_reflections(reflections)

    def set_reflections(self, reflections: dict = None):
        """
        :param reflections: A dictionary with wavelengths (µm) as keys and reflection coefficients as values.
         If None, reflections is {0.5876: 1.}
        :returns: None. Sets the reflections attribute and defines a polynomial p
         which interpolates the specified reflections coefficients.
        """
        self.reflections = reflections
        if self.reflections is None:
            self.reflections = {0.5876: 1.}
        self.p = self.determine_p()

    def sellmeier(self, wavelength: scalar) -> float:
        """
        :param wavelength: The wavelength (µm).
        :returns: The index of refraction of the material for the specified wavelength.
        """
        if self.coefficients is None:
            return self.n_real
        return float(sellmeier(wavelength, self.coefficients[0], self.coefficients[1]))

    def determine_p(self):
        """
        :returns: A polynomial which interpolates the reflection coefficients in the 'reflections' dictionary.
         The polynomial has the maximum possible order.
        """
        xy = np.array([[wave, r] for wave, r in self.reflections.items()])
        if xy.shape[0] == 1:
            return np.polynomial.polynomial.Polynomial(list(self.reflections.values()))
        poly = np.polynomial.polynomial.Polynomial.fit(xy[:, 0], xy[:, 1], xy.shape[0] - 1)
        return poly


class Node(object):
    """
    Class representing a Node in 3D-space. Defined through a label and a 3D-vector.
    """
    def __init__(self, label: str, r: array_iter):
        """
        :param label: The label of the node. Should be unique.
        :param r: The position of the node.
        """
        self.label = label
        self.r = np.asarray(r)


class Ray(object):
    """
    Class representing a light ray. A ray is a single straight line defined through a start node 'node_i'
    and an end node 'node_f' or a direction 'dr'. If neither 'node_f' nor 'dr' is given,
    'dr' is assumed to be the unit-vector in z-direction. The ray holds the properties 'power' and 'wavelength'
    as well as the material it is in.
    """
    def __init__(self, label: str, node_i: Node, node_f: Node = None, dr: array_iter = None,
                 power: scalar = 1., wavelength: scalar = 0.5876, material: Material = Material()):
        """
        :param label: The label of the ray. Should be unique.
        :param node_i: The start node of the ray.
        :param node_f: The end node of the ray.
        :param dr: The direction of the ray.
        :param power: The relative power of the ray.
        :param wavelength: The wavelength of the ray.
        :param material: The material the ray is in.
        """
        self.label = label
        self.id = int(self.label[(self.label.rfind('.')+1):])
        self.node_i = node_i
        self.node_f = node_f
        self.dr = dr
        if self.dr is None:
            if self.node_f is None:
                self.dr = np.array([0., 0., 1.])
            else:
                self.dr = self.node_f.r - self.node_i.r
        self.dr /= tools.absolute(self.dr)
        self.power = power
        self.wavelength = wavelength
        self.material = material
        self.fork = 0

    def f(self, t: ndarray) -> ndarray:
        """
        :param t: The distance from the origin of the ray, defined by 'node_i'.
        :returns: A point in 3d space which lies on the ray at a distance of 't' from its origin 'node_i.r'.
        """
        return self.node_i.r + self.dr * np.expand_dims(t, axis=-1)


class Trace(list):
    """
    A list object which contains all rays of a single cause. The properties 'halt' and 'fork' indicate
     whether the trace is complete and how often the trace has forked, respectively.
    """
    def __init__(self, label: str, rays: Iterable[Ray]):
        """
        :param label: The label of the trace. Should be unique.
        :param rays: A list of rays which have the same cause.
        """
        super().__init__(rays)
        self.label = label
        self.halt = False
        self.fork = 0

    def append(self, ray: Ray):
        """
        :param ray: The ray to append.
        :returns: None. Appends a ray to the trace.
        """
        super().append(ray)

    def plot(self):
        """
        :returns: A GLLinePlotItem, visualizing the trace.
        """
        nodes = np.array([ray.node_i.r for ray in self] + [self[-1].node_f.r])  # , self[-1].node_f.r + 1. * self[-1].dr
        return gl.GLLinePlotItem(pos=nodes, color=(0., 1., 0., 1.))


class Traces(object):
    def __init__(self, r0: array_iter, dr: array_iter):
        self.indices = np.arange(r0.shape[0], dtype=int)
        self.r0 = np.asarray(r0)
        self.dr = np.asarray(dr)
        self.nodes = [[r] for r in self.r0]
        self.dr_f = self.dr.copy()
        self.active = True
        self.nan = None

    def delete(self, indices):
        self.nan = indices
        self.r0 = np.delete(self.r0, indices, axis=0)
        self.dr = np.delete(self.dr, indices, axis=0)
        self.indices = np.delete(self.indices, indices, axis=0)


class Surface(object):
    """
    Class representing a general surface object. The shape of the surface is defined through a function f(x, y)
     over the x-y-plane at z=0. The size of the surface can be constrained through a rectangular area in the x-y-plane
     defined by 'bounds' or through an elliptic area defined
     by the upper values of 'bounds' (bounds[0][1] and bounds[1][1]).
     The surface object is first rotated using a rotation object (Tools.Rotation)
     and then shifted to the position defined by the vector 'r0'.
     Therefore, every orientation and location in the 3d-space can be achieved.
     'f' and its derivatives 'dfx' and 'dfy' have to be defined in the subclasses.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        """
        :param label: The label of the surface. Should be unique.
        :param p: The parameters passed to the surface function 'f'.
        :param r0: The origin position of the surface in 3D-space.
        :param rotation: The rotation object which defines the orientation of the surface.
        :param elliptic: Whether the base area of the surface have rectangular or elliptic shape.
        :param halt: Whether incident traces are halted.
        :param min_hits: The minimum number of surface intersections a trace must have had
         to be recognized by the surface.
        """
        self.label = label
        self.p = p
        if r0 is None:
            r0 = np.array([0., 0., 0.])
        self.r0 = np.asarray(r0)
        self.r0_gpu = np.expand_dims(r0, axis=0)
        self.rotation = rotation
        self.e_x = self.rotation.R[:, 0]
        self.e_y = self.rotation.R[:, 1]
        self.e_z = self.rotation.R[:, 2]

        self.e_x_gpu = np.expand_dims(self.e_x, axis=0)
        self.e_y_gpu = np.expand_dims(self.e_y, axis=0)
        self.e_z_gpu = np.expand_dims(self.e_z, axis=0)
        self.R_gpu = np.expand_dims(self.rotation.R, axis=0)

        self.elliptic = elliptic
        self.halt = halt
        self.min_hits = min_hits
        self.material_1 = Material()
        self.material_2 = Material()
        self.radius = 5.
        self.bounds = [[-self.radius, self.radius], [-self.radius, self.radius]]
        self.rays = set()

    def update(self, **kwargs) -> 'Surface':
        """
        :param kwargs: The keyword arguments can be any argument recognized by the constructor.
        :returns: A new surface object of the same type with the updated attributes.
        """
        for k, v in kwargs.items():
            setattr(self, k, v)
        self_new = type(self)(self.label, self.p, r0=self.r0, rotation=self.rotation,
                              elliptic=self.elliptic, halt=self.halt, min_hits=self.min_hits)
        self_new.material_1 = self.material_1
        self_new.material_2 = self.material_2
        self_new.radius = self.radius
        self_new.bounds = self.bounds
        return self_new

    def outside(self, x: ndarray, y: ndarray) -> ndarray:
        """
        :param x: A value on the local x-axis.
        :param y: A value on the local y-axis.
        :returns: A mask specifying what lies outside the bounds.
        """
        nan = np.isnan(x)  # TODO: Check.
        mask = np.full(x.shape, False)
        mask[nan] = True
        if self.elliptic:
            mask[~nan] += (x[~nan] / self.bounds[0][1]) ** 2 + (y[~nan] / self.bounds[1][1]) ** 2 > 1.
        else:
            mask_x = x[~nan] < self.bounds[0][0]
            mask_x += x[~nan] > self.bounds[0][1]
            mask_y = y[~nan] < self.bounds[1][0]
            mask_y += y[~nan] > self.bounds[1][1]
            mask[~nan] += mask_x + mask_y
        return mask

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        """
        :param x: A value on the local x-axis.
        :param y: A value on the local y-axis.
        :returns: The profile of the surface.
        """
        pass

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        """
        :param x: A value on the local x-axis.
        :param y: A value on the local y-axis.
        :returns: The derivative in the x-direction of the profile of the surface.
        """
        pass

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        """
        :param x: A value on the local x-axis.
        :param y: A value on the local y-axis.
        :returns: The derivative in the y-direction of the profile of the surface.
        """
        pass

    def xy(self, r: ndarray) -> (ndarray, ndarray):
        """
        :param r: A vector in 3D-space.
        :returns: The local x and y coordinate of a vector in 3D-space.
        """
        return np.sum(self.e_x * (r - self.r0), axis=-1), np.sum(self.e_y * (r - self.r0), axis=-1)

    def xy_gpu(self, r: ndarray) -> (ndarray, ndarray):
        """
        :param r: Vectors in 3D-space.
        :returns: The local x and y coordinate of vectors in 3D-space.
        """
        return np.sum(self.e_x_gpu * (r - self.r0_gpu), axis=-1), np.sum(self.e_y_gpu * (r - self.r0_gpu), axis=-1)

    def definition(self, r: ndarray) -> ndarray:
        """
        :param r: A vector in 3D-space.
        :returns: Zero for vectors which lie on the surface. The function is continuous.
        """
        xy = r - (self.r0 + self.e_z * np.expand_dims(self.f(*self.xy(r)), axis=-1))
        return np.sum(xy * self.e_z, axis=-1)

    def definition_gpu(self, r: ndarray) -> ndarray:
        """
        :param r: Vectors in 3D-space.
        :returns: Zero for vectors which lie on the surface. The function is continuous.
        """
        xy = r - (self.r0_gpu + self.e_z_gpu * np.expand_dims(self.f(*self.xy(r)), axis=-1))
        return np.sum(xy * self.e_z_gpu, axis=-1)

    def definition_gpu_derivative(self, r: ndarray, dr: ndarray) -> ndarray:
        """
        :param r: Vectors in 3D-space.
        :param dr: Ray directions in 3D-space.
        :returns: The derivative of the surface defining function. The function is continuous.
        """
        x, y = self.xy_gpu(r)
        xy = self.e_z_gpu - self.e_x_gpu * np.expand_dims(self.dfx(x, y), axis=-1) \
            - self.e_y_gpu * np.expand_dims(self.dfy(x, y), axis=-1)
        return np.sum(xy * dr, axis=-1)

    def normal(self, r: ndarray) -> ndarray:
        """
        :param r: A vector in 3D-space.
        :returns: The normal of the surface at the position 'r'.
        """
        x, y = self.xy(r)
        n_local = np.array([-self.dfx(x, y).squeeze(), -self.dfy(x, y).squeeze(), 1.])
        n = tools.transform(self.rotation.R, n_local)
        return n / tools.absolute(n, axis=-1)

    def normal_gpu(self, r: ndarray) -> ndarray:
        """
        :param r: Vectors in 3D-space.
        :returns: The normals of the surface at the positions 'r'.
        """
        x, y = self.xy_gpu(r)
        n_local = np.array([-self.dfx(x, y), -self.dfy(x, y), np.ones(r.shape[0])]).T
        n = tools.transform(self.rotation.R, n_local, axis=-1)
        return n / tools.absolute(n, axis=-1)

    def next(self, r: ndarray, dr: ndarray) -> ndarray:
        """
        :param r: Vectors in 3D-space.
        :param dr: Ray directions in 3D-space.
        :returns: The directions resulting from the surface intersections of incoming rays in 3D-space.
        """
        pass

    def root(self, ray: Ray) -> float:
        """
        :param ray: The incident ray.
        :returns: The distance from the rays origin to its intersection with the surface, i.e. ray.f^{-1}(r_surface).
        """
        pass

    def damping(self, ray: Ray) -> float:
        """
        :param ray: The incident ray.
        :returns: The ratio of the power of the outgoing ray and the incoming ray.
        """
        pass

    def plot(self, n: int = 32, **kwargs) -> Union[gl.GLMeshItem, None]:
        """
        :param n: The number of radial and axial vertices, giving a total of n ** 2 + 1 vertices.
        :param kwargs: Key word arguments passed to the GLMeshItem.
        :returns: A GLMeshItem representing the surface for a 3D plot. Returns None for a rectangular base area.
        """
        if self.elliptic:
            r = np.sqrt(np.linspace(0., 0.999, n + 1))[1:]
            phi = np.linspace(0., 2., n + 1)[:-1] * np.pi
            r, phi = np.meshgrid(r, phi, indexing='ij')
            x = r * self.bounds[0][1] * np.cos(phi)
            y = r * self.bounds[1][1] * np.sin(phi)
            z = self.f(x, y)
            vertexes = np.transpose(np.array([x, y, z]), axes=[1, 2, 0])
            faces = np.array([[(k + j) * n + (i + j) % n, k * n + (i + 1) % n, (k + 1) * n + i]
                              for k, vertex in enumerate(vertexes[:-1])
                              for i in range(len(vertex)) for j in [0, 1]])
            faces_top = np.array([[i, (i + 1) % n, n ** 2] for i in range(n)])
            faces = np.concatenate((faces_top, faces), axis=0)
            vertexes = vertexes.reshape((n ** 2, 3), order='C')
            vertexes = np.concatenate((vertexes, np.array([[0., 0., self.f(np.zeros(1), np.zeros(1))[0]]])), axis=0)
        else:
            return
        mesh = gl.MeshData(vertexes=vertexes, faces=faces)
        item = gl.GLMeshItem(meshdata=mesh, **kwargs)
        item.rotate(self.rotation.alpha_deg, *self.rotation.dr)
        item.translate(*self.r0)
        return item

    def plot_normals(self, n: int = 32) -> [gl.GLLinePlotItem]:
        """
        :param n: The number of radial and axial normals, giving a total of n ** 2 + 1 normals.
        :returns: A list of GLLinePlotItems representing the normals of the surface for a 3D plot.
        """
        r = np.sqrt(np.linspace(0., 0.99, n + 1))[1:]
        phi = np.linspace(0., 2., n + 1)[:-1] * np.pi
        r, phi = np.meshgrid(r, phi, indexing='ij')
        x = r * self.bounds[0][1] * np.cos(phi)
        y = r * self.bounds[1][1] * np.sin(phi)
        z = self.f(x, y)
        vectors = [np.array([x_i, y_i, z_i]) for x_i, y_i, z_i in zip(x.flatten(), y.flatten(), z.flatten())]
        return [gl.GLLinePlotItem(pos=np.array([v, v + self.normal(v)]), color=(0., 1., 1., 1.)) for v in vectors]


class Mirror(Surface):
    """
    Class representing a reflecting surface.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic, halt=halt, min_hits=min_hits)
    
    def next(self, r: ndarray, ray: Ray) -> list:
        dr_mirror = ray.dr - 2 * self.normal(r) * np.sum(self.normal(r) * ray.dr, axis=-1)
        dr_mirror = np.around(dr_mirror, decimals=8)
        return [dr_mirror / tools.absolute(dr_mirror, axis=-1)]

    def next_gpu(self, r: ndarray, dr: ndarray) -> list:
        n = self.normal_gpu(r)
        dr_mirror = dr - 2 * n * np.sum(n * dr, axis=-1)
        dr_mirror = np.around(dr_mirror, decimals=8)
        return [dr_mirror / tools.absolute(dr_mirror, axis=-1)]

    def damping(self, ray: Ray) -> float:
        return ray.material.p(ray.wavelength)


class PlaneMirror(Mirror):
    """
    Class representing a plane mirror. The surface function has no extra parameters.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic,
                         halt=halt, min_hits=min_hits)

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.zeros(x.shape)
        ret[mask] = np.nan
        return ret

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        return self.f(x, y)

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        return self.f(x, y)

    def root(self, ray: Ray) -> float:
        n = self.normal(np.array([0., 0., 0.]))
        t = np.sum(n * (self.r0 - ray.node_i.r), axis=-1) / np.sum(n * ray.dr, axis=-1)
        return t

    def plot(self, n: int = 32, **kwargs) -> gl.GLMeshItem:
        """
        :param n: The number of radial and axial normals, giving a total of n + 1 normals.
        :param kwargs: Key word arguments passed to the GLMeshItem.
        :returns: A GLMeshItem representing the surface for a 3D plot. Returns None for a rectangular base area.
        """
        if self.elliptic:
            phi = np.linspace(0., 2., n + 1)[:-1] * np.pi
            x = self.bounds[0][1] * np.cos(phi)
            y = self.bounds[1][1] * np.sin(phi)
            vertexes = np.array([x, y, np.zeros(n, dtype=float)]).T
            faces = np.array([[i, (i + 1) % n, n] for i, vertex in enumerate(vertexes)])
            vertexes = np.concatenate((vertexes, np.array([[0., 0., 0.]])), axis=0)
        else:
            vertexes = np.array([[x, y, 0.] for x in self.bounds[0] for y in self.bounds[1]])
            faces = np.array([[0, 1, 2], [1, 2, 3]])
        mesh = gl.MeshData(vertexes=vertexes, faces=faces)
        item = gl.GLMeshItem(meshdata=mesh, **kwargs)
        item.rotate(self.rotation.alpha_deg, *self.rotation.dr)
        item.translate(*self.r0)
        return item


class SphericalMirror(Mirror):
    """
    Class representing a spherical mirror. The surface function has three extra parameters.
     p[0] is the radius of the mirror, p[1] and p[2] are the x- and y-coefficient, respectively.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic,
                         halt=halt, min_hits=min_hits)

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        discriminant = self.p[0] ** 2 - (self.p[1] * x ** 2 + self.p[2] * y ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        ret[~mask] = np.sqrt(discriminant[~mask])
        return ret

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        discriminant = self.p[0] ** 2 - (self.p[1] * x ** 2 + self.p[2] * y ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        ret[~mask] = -self.p[1] * x[~mask] / np.sqrt(discriminant[~mask])
        return ret

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        discriminant = self.p[0] ** 2 - (self.p[1] * x ** 2 + self.p[2] * y ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        ret[~mask] = -self.p[2] * y[~mask] / np.sqrt(discriminant[~mask])
        return ret


class ParabolicMirror(Mirror):
    """
    Class representing a parabolic mirror. The surface function has two extra parameters.
     p[0] and p[1] are the x- and y-coefficient, respectively.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic,
                         halt=halt, min_hits=min_hits)

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.full(x.shape, self.p[0] * x ** 2 + self.p[1] * y ** 2)
        ret[mask] = np.nan
        return ret

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.full(x.shape, 2. * self.p[0] * x)
        ret[mask] = np.nan
        return ret

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.full(x.shape, 2. * self.p[1] * y)
        ret[mask] = np.nan
        return ret


class WaveMirror(Mirror):
    """
    Class representing a sinus-like mirror in the x-direction. The surface function has two extra parameters.
     p[0] is the period and p[1] is the amplitude.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic,
                         halt=halt, min_hits=min_hits)

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.full(x.shape, self.p[1] * np.sin(2. * np.pi * x / self.p[0]))
        ret[mask] = np.nan
        return ret

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.full(x.shape, 2. * np.pi / self.p[0] * self.p[1] * np.cos(2. * np.pi * x / self.p[0]))
        ret[mask] = np.nan
        return ret

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.full(x.shape, 0.)
        ret[mask] = np.nan
        return ret


class Lens(Surface):
    """
    Class representing a refracting surface.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic, halt=halt, min_hits=min_hits)
        self.material_2 = Material(label='Standard glass', n=1.46)

    def next(self, r: ndarray, ray: Ray) -> list:
        mat = self.material_1 if ray.material.label == self.material_2.label else self.material_2
        n = self.normal(r)
        n_projected = np.sum(n * ray.dr, axis=-1)
        if np.allclose(np.absolute(n_projected), 1., rtol=1e-8):
            return [ray.dr, -ray.dr]
        alpha_i = tools.angle(ray.dr, n, axis=-1)
        arg = ray.material.sellmeier(ray.wavelength) / mat.sellmeier(ray.wavelength) * np.sin(alpha_i)

        dr_mirror = ray.dr - 2 * self.normal(r) * np.sum(self.normal(r) * ray.dr, axis=-1)
        dr_mirror = np.around(dr_mirror, decimals=8)
        if arg > 1. or arg < -1.:
            return [None, dr_mirror / tools.absolute(dr_mirror, axis=-1)]

        alpha_f = np.arcsin(arg)
        dr_lens = ray.dr - n * n_projected
        dr_lens /= tools.absolute(dr_lens, axis=-1)
        n *= np.sign(n_projected)
        dr_lens *= np.tan(alpha_f)
        dr_lens += n
        return [dr_lens / tools.absolute(dr_lens, axis=-1), dr_mirror / tools.absolute(dr_mirror, axis=-1)]

    def damping(self, ray: Ray) -> float:
        n_1 = self.material_1.sellmeier(ray.wavelength)
        n_2 = self.material_2.sellmeier(ray.wavelength)
        return 1. - ((n_1 - n_2) / (n_1 + n_2)) ** 2


class PlaneLens(Lens):
    """
    Class representing a plane lens. The surface function has no extra parameters.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic, halt=halt, min_hits=min_hits)

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        ret = np.zeros(x.shape)
        ret[mask] = np.nan
        return ret

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        return self.f(x, y)

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        return self.f(x, y)

    def root(self, ray: Ray) -> float:
        n = self.normal(np.array([0., 0., 0.]))
        t = np.sum(n * (self.r0 - ray.node_i.r), axis=-1) / np.sum(n * ray.dr, axis=-1)
        return t

    def plot(self, n: int = 32, **kwargs) -> gl.GLMeshItem:
        if self.elliptic:
            phi = np.linspace(0., 2., n + 1)[:-1] * np.pi
            x = self.bounds[0][1] * np.cos(phi)
            y = self.bounds[1][1] * np.sin(phi)
            vertexes = np.array([x, y, np.zeros(n, dtype=float)]).T
            faces = np.array([[i, (i + 1) % n, n] for i, vertex in enumerate(vertexes)])
            vertexes = np.concatenate((vertexes, np.array([[0., 0., 0.]])), axis=0)
        else:
            vertexes = np.array([[x, y, 0.] for x in self.bounds[0] for y in self.bounds[1]])
            faces = np.array([[0, 1, 2], [1, 2, 3]])
        mesh = gl.MeshData(vertexes=vertexes, faces=faces)
        item = gl.GLMeshItem(meshdata=mesh, **kwargs)
        item.rotate(self.rotation.alpha_deg, *self.rotation.dr)
        item.translate(*self.r0)
        return item


class SphericalLens(Lens):
    """
    Class representing a spherical lens. The surface function has three extra parameters.
     p[0] is the radius of the lens, p[1] and p[2] are the x- and y-coefficient, respectively.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic, halt=halt, min_hits=min_hits)

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        discriminant = self.p[0] ** 2 - (self.p[1] * x ** 2 + self.p[2] * y ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        ret[~mask] = np.sqrt(discriminant[~mask])
        return ret

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        discriminant = self.p[0] ** 2 - (self.p[1] * x ** 2 + self.p[2] * y ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        ret[~mask] = -self.p[1] * x[~mask] / np.sqrt(discriminant[~mask])
        return ret

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        mask = self.outside(x, y)
        discriminant = self.p[0] ** 2 - (self.p[1] * x ** 2 + self.p[2] * y ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        ret[~mask] = -self.p[2] * y[~mask] / np.sqrt(discriminant[~mask])
        return ret


class AsphericLens(Lens):
    """
    Class representing an aspherical lens. The surface function has nine extra parameters.
     p[0] is the radius of the lens, p[1] is the hyperbolic constant,
     p[2:9] are the coefficients of a correction polynomial of orders r ** (2n), starting at n = 1.
    """
    def __init__(self, label: str, p: list, r0: array_iter = None, rotation: tools.Rotation = tools.Rotation(),
                 elliptic: bool = True, halt: bool = False, min_hits: int = 0):
        super().__init__(label, p, r0=r0, rotation=rotation, elliptic=elliptic, halt=halt, min_hits=min_hits)

    def f(self, x: ndarray, y: ndarray) -> ndarray:
        # d *= 1e-2
        # e *= 1e-5
        # f *= 1e-9
        # g *= 1e-12
        # h *= 1e-14
        # j *= 1e-16
        # l *= 1e-18
        mask = self.outside(x, y)
        r2 = x ** 2 + y ** 2
        discriminant = 1. - (1. + self.p[1]) * r2 / (self.p[0] ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        r2_m = r2[~mask]
        ret[~mask] = r2_m / self.p[0] / (1. + np.sqrt(discriminant[~mask]))
        ret[~mask] += np.sum([self.p[n + 2] * r2_m ** (n + 1) for n in range(7)], axis=0)
        return ret

    def _df(self, x: ndarray, y: ndarray) -> (ndarray, ndarray):
        """
        :param x: A value on the local x-axis.
        :param y: A value on the local y-axis.
        :returns: The part of the derivative of the profile of the surface which is common to the x- and y-axis
         and the mask where x or y lies outside of the base area.
        """
        # d *= 1e-2
        # e *= 1e-5
        # f *= 1e-9
        # g *= 1e-12
        # h *= 1e-14
        # j *= 1e-16
        # l *= 1e-18
        mask = self.outside(x, y)
        r2 = x ** 2 + y ** 2
        discriminant = 1. - (1. + self.p[1]) * r2 / (self.p[0] ** 2)
        mask += discriminant < 0.
        ret = np.full(x.shape, np.nan)
        r2_m = r2[~mask]
        ret[~mask] = 2. * (1. + np.sqrt(discriminant[~mask])) \
            + (r2_m / self.p[0] ** 2) * (1. + self.p[1]) / np.sqrt(discriminant[~mask])
        ret[~mask] /= (1. + np.sqrt(discriminant[~mask])) ** 2
        ret[~mask] += np.sum([2. * (n + 1) * self.p[n + 2] * self.p[0] * r2_m ** n for n in range(7)], axis=0)
        ret[~mask] /= 2. * self.p[0]
        return ret, mask

    def dfx(self, x: ndarray, y: ndarray) -> ndarray:
        ret, mask = self._df(x, y)
        ret[~mask] = 2. * ret[~mask] * x[~mask]
        return ret

    def dfy(self, x: ndarray, y: ndarray) -> ndarray:
        ret, mask = self._df(x, y)
        ret[~mask] = 2. * ret[~mask] * y[~mask]
        return ret

    def scaled(self, scale):
        """
        :param scale: The scale of the new lens.
        :returns: A new aspheric lens scaled by 'scale'.
        """
        kwargs = {'p': [self.p[0] * scale, self.p[1], ] + [p_n / (scale ** (2 * (n + 1) - 1))
                                                           for n, p_n in enumerate(self.p[2:])],
                  'r0': self.r0 * scale}
        self_scaled = self.update(**kwargs)
        self_scaled.bounds = [[self.bounds[0][0] * scale, self.bounds[0][1] * scale],
                              [self.bounds[1][0] * scale, self.bounds[1][1] * scale]]
        return self_scaled


class Geometry(list):
    """
    A list object which contains all surfaces as well as the boundaries of the scene.
    The scene is always sphere-shaped with a 'center' and a 'radius'.
    """
    def __init__(self, surfaces: Iterable[Surface], center: array_iter = None, radius: scalar = None):
        """
        :param surfaces: A list of surfaces included in the scene.
        :param center: The center of the scene.
        :param radius: The radius of the scene.
        """
        super().__init__(surfaces)
        self.labels = [surface.label for surface in surfaces]
        if center is None:
            center = [0., 0., 0.]
        self.center = np.asarray(center)
        self.radius = radius
        if self.radius is None:
            self.radius = 150.
        self.materials = [[surface.material_1.label, surface.material_2.label] for surface in self]
        self.min_hits = [surface.min_hits for surface in self]

    def append(self, surface: Surface):
        """
        :param surface: The surface which is added to the scene.
        :returns: None. Adds a surface to the scene.
        """
        super().append(surface)
        self.labels.append(surface.label)
        self.materials.append([surface.material_1.label, surface.material_2.label])
        self.min_hits.append(surface.min_hits)

    def get_surface(self, label: str) -> Surface:
        """
        :param label: The label of the surface to be returned.
        :returns: The surface of the scene with the specified 'label'.
        :raises ValueError: If the surface with the specified 'label' is not part of the scene.
        """
        flag = False
        s = None
        for s in self:
            if s.label == label:
                flag = True
                break
        if flag:
            return s
        else:
            raise ValueError('Surface {} not found.'.format(label))

    def replace_surface(self, label: str, surface: Surface):
        """
        :param label: The label of the surface to be replaced.
        :param surface: The surface which replaces the surface with the specified 'label'.
        :returns: None. Replaces a surfaces of the scene with a new one.
        :raises ValueError: If the surface with the specified 'label' is not part of the scene.
        """
        flag = False
        for i, s in enumerate(self):
            if s.label == label:
                self.remove(s)
                self.labels.pop(i)
                self.materials.pop(i)
                self.min_hits.pop(i)
                flag = True
                break
        if flag:
            self.append(surface)
        else:
            raise ValueError('Surface {} not found.'.format(label))

    def intersection(self, t: ndarray, mask: ndarray, f: Callable) -> (float, Surface):
        """
        :param t: A sample array of square roots of the distance from the origin of a ray.
        :param mask: A mask specifying which surface are included in the search for the closest intersection point.
        :param f: The f-function of a ray.
        :returns: The distance from the origin of a ray to the closest surface intersection,
         the surface with the closest intersection point and the index of that surface.
        """
        def root(s: Surface, m: bool) -> (float, Any):
            if not m:
                return np.nan

            def zero(t_i: ndarray) -> ndarray:
                return s.definition(f(t_i ** 2))

            y = zero(t)
            nans, x = tools.nan_helper(y)
            if np.all(nans):
                return np.nan
            if np.any(nans):
                y[nans] = np.interp(x(nans), x(~nans), y[~nans])
            j = np.argmax(y > 0.) if y[0] < 0. else np.argmax(y < 0.)
            if j == 0:
                return np.nan
            t_min = t[j - 1]
            t_max = t[j]
            try:
                # noinspection PyTypeChecker
                return so.brentq(zero, t_min, t_max)
            except ValueError:
                return np.nan
            # except RuntimeError:
            #     return np.nan

        results = list(map(root, self, mask))
        try:
            i = int(np.nanargmin(results))
        except ValueError:
            return np.nan, None, -1
        return results[i] ** 2, self[i], i


class Body(Geometry):  # TODO: Implementation.
    """
    A list object which contains all surfaces as well as the boundaries of the scene.
    The scene is always sphere-shaped with a 'center' and a 'radius'.
    """

    def __init__(self, surfaces: Iterable[Surface], center: array_iter = None, radius: scalar = None):
        super().__init__(surfaces, center=center, radius=radius)


class GeometryGPU(Geometry):  # TODO: Implementation.
    """
    A list object which contains all surfaces as well as the boundaries of the scene.
    The scene is always sphere-shaped with a 'center' and a 'radius'.
    """
    def __init__(self, surfaces: Iterable[Surface]):
        super().__init__(surfaces)

    def next(self):
        pass


class Source(object):
    """
    A class representing a general ray source which has a method 'create'
     to initialize an user-specified number of traces and their respective first ray.
    """
    def __init__(self, label: str, r0: array_iter = None, wavelength: scalar = 0.5876, material: Material = Material(),
                 seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: A seed for the random number generator.
        """
        self.label = label
        self.r0 = r0
        if r0 is None:
            self.r0 = np.array([0., 0., 0.])
        self.r0 = np.asarray(self.r0)
        self.wavelength = wavelength
        self.material = material
        self.seed = seed
        self.rng = np.random.RandomState(seed)

    def create(self, n: int) -> list:
        """
        :param n: The number of traces to create.
        :returns: The created traces.
        """
        pass


class ArraySource(Source):
    """
    Class representing an array of sources.
     A 'source' can be specified which is placed at the specified 'coordinates'.
    """
    def __init__(self, label: str, source: Source, coordinates: array_iter, r0: array_iter = None,
                 wavelength: scalar = 0.5876, material: Material = Material(), seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param source: The source which is placed at the specified 'coordinates'.
        :param coordinates: A list of coordinates where the 'source' is placed.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: A seed for the random number generator.
        """
        super().__init__(label, r0=r0, wavelength=wavelength, material=material, seed=seed)
        self.source = source
        self.coordinates = np.asarray(coordinates)
        if len(self.coordinates.shape) == 1:
            self.coordinates = np.expand_dims(self.coordinates, axis=0)

    def create(self, n: int) -> list:
        traces = []
        for c in self.coordinates:
            self.source.r0 = c
            traces += self.source.create(n)
        return traces


class SingleRaySource(Source):
    """
    Class representing a source of a single trace. A directional vector 'dr' can be specified.
    """
    def __init__(self, label: str, dr: array_iter = None, r0: array_iter = None, wavelength: scalar = 0.5876,
                 material: Material = Material(), seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param dr: The direction in which the ray is sent.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: Disabled
        """
        super().__init__(label, r0=r0, wavelength=wavelength, material=material, seed=seed)
        if dr is None:
            dr = [0., 0., 1.]
        self.dr = np.asarray(dr)

    def create(self, n: int) -> list:
        """
        :param n: Disabled.
        :returns: The created trace.
        """
        return [Trace('{}.0'.format(self.label), [Ray('{}.0.0'.format(self.label),
                                                      Node('{}.0.0.i'.format(self.label), self.r0), dr=self.dr,
                                                      wavelength=self.wavelength, material=self.material)])]


class ApertureSource(Source):
    """
    Class representing a source of two traces. Two directional vectors 'dr1' and 'dr2' can be specified.
    """
    def __init__(self, label: str, dr1: array_iter = None, dr2: array_iter = None,
                 r0: array_iter = None, wavelength: scalar = 0.5876, material: Material = Material(), seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param dr1: The direction in which the first ray is sent.
        :param dr2: The direction in which the second ray is sent.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: Disabled.
        """
        super().__init__(label, r0=r0, wavelength=wavelength, material=material, seed=seed)
        if dr1 is None:
            dr1 = [0., 0., 1.]
        if dr2 is None:
            dr2 = [0., 0., 1.]
        self.dr1, self.dr2 = np.asarray(dr1), np.asarray(dr2)
        self.alpha = tools.angle(dr1, dr2)
        self.NA = self.material.sellmeier(self.wavelength) * np.sin(self.alpha / 2.)

    def create(self, n: int) -> list:
        """
        :param n: Disabled.
        :returns: The created trace.
        """
        return [Trace('{}.{}'.format(self.label, num), [Ray('{}.{}.0'.format(self.label, num),
                                                        Node('{}.{}.0.i'.format(self.label, num), self.r0), dr=dr,
                                                        wavelength=self.wavelength, material=self.material)])
                for dr, num in zip([self.dr1, self.dr2], ['0', '1'])]


class IsotropicSource(Source):
    """
    Class representing an isotropic source.
    """
    def __init__(self, label: str, r0: array_iter = None, wavelength: scalar = 0.5876, material: Material = Material(),
                 seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: A seed for the random number generator.
        """
        super().__init__(label, r0=r0, wavelength=wavelength, material=material, seed=seed)

    def create(self, n: int) -> list:
        return [Trace('{}.{}'.format(self.label, i),
                      [Ray('{}.{}.0'.format(self.label, i), Node('{}.{}.0.i'.format(self.label, i), self.r0), dr=dr,
                           wavelength=self.wavelength, material=self.material)])
                for i, dr in enumerate(st.norm.rvs(size=(n, 3), random_state=self.rng))]


class DeterministicIsotropicSource(Source):
    """
    Class representing an isotropic source with regular directions.
    """
    def __init__(self, label: str, r0: array_iter = None, wavelength: scalar = 0.5876, material: Material = Material(),
                 seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: A seed for the random number generator.
        """
        super().__init__(label, r0=r0, wavelength=wavelength, material=material, seed=seed)

    def create(self, n: int) -> list:
        """
        :param n: The number of traces to create. 'n' is rounded to the next smaller cubic number.
        :returns: The created traces.
        """
        x = np.linspace(-1., 1., int(n ** (1./3.)))
        y = np.linspace(-1., 1., int(n ** (1./3.)))
        z = np.linspace(-1., 1., int(n ** (1./3.)))
        x, y, z = np.meshgrid(x, y, z, indexing='ij')
        xyz = np.array([x.flatten(), y.flatten(), z.flatten()]).T
        return [Trace('{}.{}'.format(self.label, i),
                      [Ray('{}.{}.0'.format(self.label, i), Node('{}.{}.0.i'.format(self.label, i), self.r0), dr=dr,
                           wavelength=self.wavelength, material=self.material)])
                for i, dr in enumerate(xyz)]


class IsotropicCylinderSource(Source):
    """
    Class representing an isotropic source in a cylinder volume.
    """
    def __init__(self, label: str, length: float, radius: float, rotation: tools.Rotation = tools.Rotation(),
                 r0: array_iter = None, wavelength: scalar = 0.5876,
                 material: Material = Material(), seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param length: The length of the cylinder along the x-axis.
        :param radius: The radius of the cylinder.
        :param rotation: The rotation object which defines the orientation of the source.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: A seed for the random number generator.
        """
        super().__init__(label, r0=r0, wavelength=wavelength, material=material, seed=seed)
        self.length = length
        self.radius = radius
        if rotation is None:
            rotation = tools.Rotation(0., np.array([0., 0., 1.]))
        self.rotation = rotation

    def create(self, n: int) -> list:
        x = st.uniform.rvs(loc=-0.5 * self.length, scale=self.length, size=n, random_state=self.rng)
        r = np.sqrt(st.uniform.rvs(loc=0., scale=self.radius ** 2, size=n, random_state=self.rng))
        alpha = st.uniform.rvs(loc=0., scale=2., size=n, random_state=self.rng) * np.pi
        y = r * np.sin(alpha)
        z = r * np.cos(alpha)
        r = tools.transform(np.expand_dims(self.rotation.R, axis=0), np.array([x, y, z]).T, axis=-1)
        dr = st.uniform.rvs(size=(n, 3), random_state=self.rng) * 2. - 1.
        return [Trace('{}.{}'.format(self.label, i),
                      [Ray('{}.{}.0'.format(self.label, i),
                           Node('{}.{}.0.i'.format(self.label, i), self.r0 + r), dr=dr,
                           wavelength=self.wavelength, material=self.material)])
                for i, (r, dr) in enumerate(zip(r, dr))]


class FixedDirectionCylinderSource(IsotropicCylinderSource):
    """
    Class representing a source which emits in a fixed direction 'dr' inside a cylinder volume.
    """
    def __init__(self, label: str, dr: array_iter, length: float, radius: float,
                 rotation: tools.Rotation = tools.Rotation(), r0: array_iter = None,
                 wavelength: scalar = 0.5876, material: Material = Material(), seed: int = None):
        """
        :param label: The label of the source. Should be unique.
        :param dr: The direction in which the rays are sent.
        :param length: The length of the cylinder along the x-axis.
        :param radius: The radius of the cylinder.
        :param rotation: The rotation object which defines the orientation of the source.
        :param r0: The position of the source in 3D-space.
        :param wavelength: The wavelength of the light the source is emitting.
        :param material: The material the source is located in. The default material is 'Vacuum'.
        :param seed: A seed for the random number generator.
        """
        super().__init__(label, length, radius, rotation=rotation, r0=r0,
                         wavelength=wavelength, material=material, seed=seed)
        self.dr = dr

    def create(self, n: int) -> list:
        x = st.uniform.rvs(loc=-0.5 * self.length, scale=self.length, size=n, random_state=self.rng)
        r = np.sqrt(st.uniform.rvs(loc=0., scale=self.radius, size=n, random_state=self.rng))
        alpha = st.uniform.rvs(loc=0., scale=2., size=n, random_state=self.rng) * np.pi
        y = r * np.sin(alpha)
        z = r * np.cos(alpha)
        r = tools.transform(np.expand_dims(self.rotation.R, axis=0), np.array([x, y, z]).T, axis=-1)
        return [Trace('{}.{}'.format(self.label, i),
                      [Ray('{}.{}.0'.format(self.label, i),
                           Node('{}.{}.0.i'.format(self.label, i), self.r0 + r), dr=self.dr,
                           wavelength=self.wavelength, material=self.material)])
                for i, r in enumerate(r)]


def cost_power(rays: list, n: int) -> float:
    return -np.sum([ray.power for ray in rays]) / n * 100


def get_zero(r0, dr, surface: Surface):
    def zero(t):
        return surface.definition_gpu(straight3d(t ** 2, r0, dr))

    def zero_jac(t):
        return surface.definition_gpu_derivative(straight3d(t ** 2, r0, dr), dr) * t * 2.

    return zero, zero_jac


def get_zero_min(r0, dr, surface: Surface):
    def zero(t):
        return np.sum(surface.definition_gpu(straight3d(t ** 2, r0, dr)) ** 2, axis=0)

    def zero_jac(t):
        return 2. * surface.definition_gpu(straight3d(t ** 2, r0, dr)) \
               * surface.definition_gpu_derivative(straight3d(t ** 2, r0, dr), dr) * t * 2.

    return zero, zero_jac


class Propagation(object):
    """
    Class representing a propagation object which holds a source and a geometry. The method 'propagate'
     starts the tracing of already existing rays or newly created rays if none existed.
     The traces are stored in 'traces'. The scene and all traces can be displayed with the 'plot'-method.
     The number of sub-processes created when ray-tracing can be specified via 'n_p'.
     In particular the speed of ray-tracing with a large number of rays benefits from a larger number of processes.
     Surfaces can be optimized with the 'optimize_surface'-method by specifying a cost function
     which fits the appropriate needs.
    """
    def __init__(self, source: Source, geometry: Geometry):
        """
        :param source: The source of the ray propagation.
        :param geometry: The geometry in which the ray propagation is executed.
        """
        self.source = source
        self.geometry = geometry
        self.traces: Union[list, Traces, None] = None
        self.iter_max = 5
        self.fork_max = 0
        self.power_min = 0.01
        self.n_p = 1
        self.vis = None

    def plot(self, draw_axes: bool = False, draw_grid: bool = False, draw_normals: bool = False,
             gpu: bool = False, surface_label: str = None):
        """
        :param draw_axes: Whether to draw axes.
        :param draw_grid: Whether to draw a coordinate grid.
        :param draw_normals: Whether to draw normals. This can cost much performance.
        :param gpu: Whether the ray-tracing was performed in gpu mode.
        :param surface_label: If specified, only rays intersecting the surface with the given label are drawn.
        :returns: None. Shows the scene.
        """
        if surface_label is None:
            surface_label = ''
        if self.vis is None:
            self.vis = Visualizer3D('Ray-Tracing Scene')
        kwargs = {'color': (0.8, 0.8, 0.9, 1.), 'edgeColor': (0., 0., 0., 1.),
                  'drawFaces': True, 'drawEdges': False, 'smooth': False, 'computeNormals': False}
        if draw_axes:
            axis = gl.GLAxisItem()
            axis.setSize(x=10., y=10., z=10.)
            self.vis.add_item(axis)
        if draw_grid:
            grid = gl.GLGridItem()
            grid.setSize(x=self.geometry.radius, y=self.geometry.radius, z=self.geometry.radius)
            grid.setSpacing(x=10., y=10., z=10.)
            self.vis.add_item(grid)
        for surface in self.geometry:
            item = surface.plot(**kwargs)  # Implement an individual MeshData object for a fancier visualization.
            if item is None:
                x = np.linspace(1. * surface.bounds[0][0], 1. * surface.bounds[0][1], 33)
                y = np.linspace(1. * surface.bounds[1][0], 1. * surface.bounds[1][1], 33)
                z = surface.f(*np.meshgrid(x, y, indexing='ij'))
                item = gl.GLSurfacePlotItem(x, y, z, **kwargs)
                item.rotate(surface.rotation.alpha_deg, *surface.rotation.dr)
                item.translate(*surface.r0)
            item.setGLOptions('translucent')
            self.vis.add_item(item)
            if draw_normals:
                items = surface.plot_normals(n=16)
                for item in items:
                    item.translate(*surface.r0)
                    item.rotate(surface.rotation.alpha_deg, *surface.rotation.dr)
                    self.vis.add_item(item)
        if gpu:
            for nodes, dr in zip(self.traces.nodes, self.traces.dr_f):
                self.vis.add_item(gl.GLLinePlotItem(pos=np.asarray(nodes + [dr]), color=(0., 1., 0., 1.)))
        else:
            if surface_label != '':
                rays = self.geometry.get_surface(surface_label).rays
                if rays == set():
                    self.vis.show()
                    return
                for trace in self.traces:
                    if trace[-1].label in rays:
                        self.vis.add_item(trace.plot())
                start_end = np.array([[[eval('trace[{}].node_{}.r'.format(-i, node))] for trace in self.traces
                                       if trace[-1].label in rays]
                                      for i, node in enumerate('if')])
            else:
                for trace in self.traces:
                    self.vis.add_item(trace.plot())
                # noinspection PyUnusedLocal
                start_end = np.array([[[eval('trace[{}].node_{}.r'.format(-i, node))] for trace in self.traces]
                                      for i, node in enumerate('if')])
            starts = gl.GLScatterPlotItem(pos=start_end[0], color=(0., 1., 0., 1.), size=5)
            ends = gl.GLScatterPlotItem(pos=start_end[1], color=(1., 0., 0., 1.), size=5)
            self.vis.add_item(starts)
            self.vis.add_item(ends)
        self.vis.show()

    def get_rays(self, labels):
        """
        :param labels: A list of ray labels.
        :returns: The rays whose label is in the list 'labels'.
        """
        if self.traces is None:
            return []
        return [ray for trace in self.traces for ray in trace if ray.label in labels]

    def create(self, n: int):
        """
        :param n: The number of traces to create.
        :returns: None. Saves the created traces in the 'traces' attribute.
        """
        self.traces = self.source.create(n)

    def _surface_loop(self, ray: Ray) -> (list, list):
        """
        :param ray: The ray whose surface intersections are checked.
        :returns: The distance from the origin of the 'ray' to the closest surface intersection,
         the surface with the closest intersection point and the index of that surface.
        """
        t_bounds = sphere_intersection(self.geometry.center, self.geometry.radius, ray.node_i.r, ray.dr)
        t_array = np.linspace(0., np.sqrt(t_bounds[1][0]), 101)
        min_hits_mask = ray.id >= np.array(self.geometry.min_hits)
        return self.geometry.intersection(t_array, min_hits_mask, ray.f)

    def _trace_loop(self, traces: list, q: mp.Queue = None, shared: list = None):
        """
        :param traces: The traces to propagate.
        :param q: A queue to store the traces in when the propagation has finished. Used for multiprocessing.
        :param shared: A list to save the information which ray intersected which surface. Used for multiprocessing.
        :returns: None. Iteratively propagates the traces.
        """
        total = 0.
        tt = 0.
        n = 0
        surface_rays = {surface.label: set() for surface in self.geometry}
        not_finished = np.array([not trace.halt for trace in traces])
        while not_finished.any() and n < self.iter_max:
            n += 1
            new_traces = []
            for trace in it.compress(traces, not_finished):
                ray = trace[-1]
                start = time()
                t, surface, i = self._surface_loop(ray)
                total += time() - start
                start_tt = time()
                if surface is None:
                    ray.node_f = Node(ray.node_i.label[:-1] + 'f', ray.node_i.r + 5 * ray.dr)
                    trace.halt = True
                    continue
                if shared is None:
                    surface.rays.add(ray.label)
                else:
                    surface_rays[surface.label].add(ray.label)
                power = surface.damping(ray) * ray.power
                r0_new = ray.f(t)
                ray.node_f = Node('{}.f'.format(ray.label), r0_new)
                if surface.halt or ray.material.label not in self.geometry.materials[i]:
                    trace.halt = True
                    continue
                dr_new_list = surface.next(r0_new, ray)
                dr_new = dr_new_list[0]
                if dr_new is not None and power >= self.power_min:
                    mat = surface.material_1 if ray.material.label == surface.material_2.label else surface.material_2
                    ray_new = Ray('{}.{}'.format(trace.label, ray.id + 1),
                                  Node('{}.{}.i'.format(trace.label, ray.id + 1), r0_new + 1e-5 * dr_new),
                                  dr=dr_new, power=power, wavelength=ray.wavelength, material=mat)
                    ray_new.fork = ray.fork
                    ray_new.id = ray.id + 1
                    trace.append(ray_new)
                else:
                    trace.halt = True
                if len(dr_new_list) > 1 and ray.fork < self.fork_max and ray.power - power >= self.power_min:
                    trace.fork += 1
                    dr_sec = dr_new_list[1]
                    ray_sec = Ray('{}s{}f{}.{}'.format(trace.label, trace.fork, ray.fork + 1, ray.id + 1),
                                  Node('{}s{}f{}.{}.i'.format(trace.label, trace.fork, ray.fork + 1, ray.id + 1),
                                       r0_new + 1e-5 * dr_sec), dr=dr_sec,
                                  power=ray.power - power,  wavelength=ray.wavelength, material=ray.material)
                    ray_sec.fork = ray.fork + 1
                    ray_sec.id = ray.id + 1
                    new_traces.append(Trace('{}s{}f{}'.format(trace.label, trace.fork, ray_sec.fork), [ray_sec]))
                    new_traces[-1].fork = trace.fork
                tt += time() - start_tt
            traces += new_traces
            not_finished = np.array([not trace.halt for trace in traces])
            # print('-- {} / {} --'.format(n, self.iter_max), len(traces))
        for j, trace in enumerate(it.compress(traces, not_finished)):
            trace[-1].node_f = trace[-1].node_i
            trace[-1].halt = True
        if q is not None:
            q.put(traces)
        if shared is not None:
            shared.append(surface_rays)
        print('Surface loop: ', total)
        print('Continue time: ', tt)
        print('Sum: ', tt)

    def _trace_loop_gpu(self, traces: list) -> (list, list):
        """
        :param traces:
        :returns:
        """
        traces_gpu = Traces(np.array([trace[0].node_i.r for trace in traces]),
                            np.array([trace[0].dr for trace in traces]))
        tt = 0.
        n = 0
        while traces_gpu.active and n < self.iter_max:
            n += 1
            # t_bounds = sphere_intersection(self.geometry.center, self.geometry.radius, traces_gpu.r0, traces_gpu.dr)
            t_list = []
            s_list = []
            t_bounds = sphere_intersection(self.geometry.center, self.geometry.radius, traces_gpu.r0, traces_gpu.dr)
            t_sample = np.linspace(np.zeros(traces_gpu.r0.shape[0]), np.sqrt(t_bounds[1]), 101)
            for surface in self.geometry:
                start = time()
                zero, zero_jac = get_zero(traces_gpu.r0, traces_gpu.dr, surface)
                # get_intersection(zero, zero_jac, surface) TODO
                sample = zero(t_sample)
                mask = sample[0] < 0.
                mask = mask.astype(bool)
                i = np.nanargmax(sample > 0., axis=0)
                i[~mask] = np.nanargmax(sample < 0., axis=0)[~mask]
                t0 = np.take_along_axis(t_sample, np.expand_dims(i - 1, axis=0), axis=0)[0]
                t1 = np.take_along_axis(t_sample, np.expand_dims(i, axis=0), axis=0)[0]
                nan = np.isnan(zero(t0))
                nan += np.sign(zero(t0)) == np.sign(zero(t1))
                # t0 = np.full(traces_gpu.r0.shape[0], 7.)
                root = np.full(traces_gpu.r0.shape[0], np.nan)

                # root, converged, zero_der = so.newton(zero, t0, fprime=zero_jac, full_output=True, maxiter=10)
                # root = so.minimize(zero, x0=t0, jac=zero_jac)

                def zero_brent(ttt: ndarray, r: ndarray, dr: ndarray) -> ndarray:
                    return surface.definition_gpu(straight3d(ttt ** 2, r, dr))

                # noinspection PyTypeChecker
                root[~nan] = np.array([so.brentq(zero_brent, t0_i, t1_i, args=(r_i, dr_i))
                                       for t0_i, t1_i, r_i, dr_i
                                       in zip(t0[~nan], t1[~nan], traces_gpu.r0[~nan], traces_gpu.dr[~nan])])
                t_list.append(root)
                s_list.append(surface)
                stop = time()
                tt += stop - start
            t_list, s_list = np.asarray(t_list), np.asarray(s_list)
            nan = np.isnan(t_list)
            nan = ~np.sum(~nan, axis=0).astype(bool)
            traces_gpu.delete(nan)
            t_list = np.delete(t_list, nan, axis=1)
            if t_list.shape[1] == 0:
                traces_gpu.active = False
                break
            i = np.nanargmin(t_list, axis=0)
            t = np.take_along_axis(t_list, np.expand_dims(i, axis=0), axis=0)[0]
            r0_next = straight3d(t ** 2, traces_gpu.r0, traces_gpu.dr)
            dr_next = np.array([s_list[j].next(r0, dr) for j, r0, dr in zip(i, r0_next, traces_gpu.dr)])
            r0_next += 1e-5 * dr_next
            traces_gpu.r0 = r0_next
            traces_gpu.dr = dr_next
            for j, r0, dr in zip(traces_gpu.indices, r0_next, dr_next):
                traces_gpu.nodes[j].append(r0)
                traces_gpu.dr_f[j] = dr
        print('Root-finding time: ', tt)

    def propagate(self, show: bool = False, gpu: bool = False, surface_label: str = None):
        """
        :param show: Whether to show the result after propagation.
        :param gpu: Whether the propagation is performed in the gpu mode
        :param surface_label: If specified, only rays intersecting the surface with the given label are drawn.
        :returns: None. Sets up and runs the ray propagation.
        """
        if self.traces is None:
            self.create(1)
        if gpu:
            self._trace_loop_gpu(self.traces)
            if show:
                self.plot(gpu=True)
            return
        if self.n_p == 1:
            start = time()
            self._trace_loop(self.traces, q=None, shared=None)
            print('Trace time: ', time() - start)
        elif self.n_p > 1:
            if self.n_p > mp.cpu_count():
                print('Number of desired sub-processes exceeds number of available cpu cores.'
                      ' Changing \'self.n_p\' to {}'.format(mp.cpu_count()))
                self.n_p = mp.cpu_count()
            q = mp.Queue()
            manager = mp.Manager()
            shared = manager.list()
            traces = []
            processes = []
            for i in range(self.n_p):
                mod = len(self.traces) % self.n_p
                j = int(i * len(self.traces) / self.n_p)
                k = int((i + 1) * len(self.traces) / self.n_p)
                t = self.traces[j:k]
                if i == self.n_p - 1:
                    t += self.traces[k:(k+mod)]
                processes.append(mp.Process(target=self._trace_loop, args=(t, q, shared)))
            for p in processes:
                start = time()
                p.start()
                stop = time()
                print(stop - start)
            for _ in processes:
                traces += q.get()
            for p in processes:
                p.join()
            self.traces = traces
            for shared_surfaces in shared:
                for surface in self.geometry:
                    surface.rays.update(shared_surfaces[surface.label])
        else:
            raise ValueError('Please specify a positive integer for the desired number of sub-processes.')

        if show:
            self.plot(surface_label=surface_label)

    def optimize_surface(self, cost_func: Callable, surface_labels: list, p0: list, fixed: list,
                         analysis_label: str, n: int = 100) -> ndarray:
        """
        :param cost_func: The cost function to optimize a surface.
        :param surface_labels: A list of surfaces to optimize.
        :param p0: A list of the initial parameters for the surfaces. The parameters for each surface
         must be stored in a dict as keyword arguments for the constructor of the respective surface.
        :param fixed: A list with the information which parameters stay fixed.
         'fixed' must have the same structure as p0.
        :param analysis_label: The label of the surface on which the 'cost_function' is evaluated.
        :param n: The number of traces used for the ray-tracing.
        :returns: The optimal parameters.
        """
        for s_label, s_p0 in zip(surface_labels, p0):
            self.geometry.replace_surface(s_label, self.geometry.get_surface(s_label).update(**s_p0))
        par = [np.array(list(s_p0['p']) + list(s_p0['r0'])) for s_p0 in p0]
        par_f = [np.array(list(s_p0['p']) + list(s_p0['r0'])) for s_p0 in fixed]

        def cost(x):
            self.source.rng = np.random.RandomState(self.source.seed)
            par_x = np.zeros(par[0].shape[0])
            for i, s_l in enumerate(surface_labels):
                par_x[par_f[i]] = par[i][par_f[i]]
                par_x[~par_f[i]] = x
                kwargs = {'p': par_x[:-3].tolist(), 'r0': par_x[-3:].tolist()}
                self.geometry.replace_surface(s_l, self.geometry.get_surface(s_l).update(**kwargs))

            self.create(n)
            self.propagate(show=False)
            analysis = self.geometry.get_surface(analysis_label)
            rays = self.get_rays(analysis.rays)
            c = cost_func(rays, n)
            print(len(rays), x, c)
            return c

        result = so.minimize(cost, np.concatenate([p[~p_f] for p, p_f in zip(par, par_f)], axis=0),
                             method='Nelder-Mead')
        return result.x


def test_trace_loop_gpu(n=100):
    source = IsotropicSource('Isotropic')
    s_radius = 45.
    mirror = SphericalMirror('Spherical', [s_radius, 1., 1.], r0=[0., 0., 0.], elliptic=True)
    mirror.bounds = [[s_radius, s_radius], [-s_radius, s_radius]]
    o_radius = 37.5
    plane = PlaneMirror('Plane', [], r0=[0., 0., -80.], elliptic=True, halt=True, min_hits=2)
    plane.bounds = [[-o_radius, o_radius], [-o_radius, o_radius]]
    r0 = -21.15
    radius = 25.
    lens = AsphericLens('Aspheric', [18.339, -1.099272, 0., 1.094492e-5, 9.288686e-9,
                                     -5.645807e-12, 1.501010e-14, 0., 0.], r0=[0., 0., r0 - 27.5], elliptic=True)
    lens.scale = 1.
    lens_bottom = PlaneLens('Aspheric_bottom', [], r0=[0., 0., r0])
    lens.bounds = [[-radius, radius], [-radius, radius]]
    lens_bottom.bounds = [[-radius, radius], [-radius, radius]]
    lens.n_1 = 1.459
    lens_bottom.n_2 = 1.459
    geometry = Geometry([mirror, lens, lens_bottom, plane])
    propagation = Propagation(source, geometry)
    propagation.create(n)
    # propagation._trace_loop_gpu(propagation.traces)
    propagation.propagate(show=True)
