# Copyright 2024 Luminary Cloud, Inc. All Rights Reserved.
from dataclasses import dataclass, field
from luminarycloud._proto.client import simulation_pb2 as clientpb
from luminarycloud.params.boundary_conditions.fluid import BoundaryCondition
from luminarycloud.params.boundary_conditions._proto import _bc_from_proto
from luminarycloud.params.physics import Physics
from luminarycloud.params._param_wrappers.fluid import Fluid as _Fluid


@dataclass(kw_only=True)
class Fluid(Physics, _Fluid):
    """Fluid flow physics configuration."""

    boundary_conditions: list[BoundaryCondition] = field(default_factory=list)
    "List of boundary conditions."

    def _to_proto(self) -> clientpb.Physics:
        _proto = super()._to_proto()
        _proto.fluid.CopyFrom(_Fluid._to_proto(self))
        _proto.fluid.boundary_conditions_fluid.extend(
            v._to_proto() for v in self.boundary_conditions
        )
        return _proto

    def _from_proto(self, proto: clientpb.Physics):
        super()._from_proto(proto)
        _Fluid._from_proto(self, proto.fluid)
        self.boundary_conditions = [
            _bc_from_proto(bc) for bc in proto.fluid.boundary_conditions_fluid
        ]
