# Copyright 2024 Luminary Cloud, Inc. All Rights Reserved.
from dataclasses import dataclass

from luminarycloud.types import Vector3


class Shape:
    pass


@dataclass(kw_only=True)
class Sphere(Shape):
    center: Vector3
    radius: float


@dataclass(kw_only=True)
class SphereShell(Shape):
    center: Vector3
    radius: float
    radius_inner: float


@dataclass(kw_only=True)
class HalfSphere(Shape):
    center: Vector3
    radius: float
    normal: Vector3


@dataclass(kw_only=True)
class Cube(Shape):
    min: Vector3
    max: Vector3


@dataclass(kw_only=True)
class OrientedCube(Shape):
    min: Vector3
    max: Vector3
    origin: Vector3
    x_axis: Vector3
    y_axis: Vector3
    z_axis: Vector3


@dataclass(kw_only=True)
class Cylinder(Shape):
    start: Vector3
    end: Vector3
    radius: float


@dataclass(kw_only=True)
class AnnularCylinder(Shape):
    start: Vector3
    end: Vector3
    radius: float
    radius_inner: float


@dataclass(kw_only=True)
class Torus(Shape):
    center: Vector3
    normal: Vector3
    major_radius: float
    minor_radius: float


@dataclass(kw_only=True)
class Cone(Shape):
    start: Vector3
    end: Vector3
    radius: float
