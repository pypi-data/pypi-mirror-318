# Copyright 2023-2024 Luminary Cloud, Inc. All Rights Reserved.
from datetime import datetime
from ._wrapper import ProtoWrapper, ProtoWrapperBase
from ._client import get_default_client
from ._helpers.timestamp_to_datetime import timestamp_to_datetime
from ._proto.api.v0.luminarycloud.geometry import geometry_pb2 as geometrypb
from ._proto.geometry import geometry_pb2 as gpb

from .params.geometry import Surface, Volume
from .types import Vector3


@ProtoWrapper(geometrypb.Geometry)
class Geometry(ProtoWrapperBase):
    """Represents a Geometry object."""

    id: str
    "Geometry ID."
    name: str
    "Geometry name."

    _proto: geometrypb.Geometry

    @property
    def create_time(self) -> datetime:
        """
        The time the geometry was created.
        """
        return timestamp_to_datetime(self._proto.create_time)

    def modify(
        self, modification: gpb.Modification
    ) -> tuple[list[gpb.Volume], list[gpb.Feature], list[gpb.FeatureIssues]]:
        """
        Apply a modification to the geometry.

        Parameters
        ----------
        modification : Modification
            The modification to apply to the geometry.

        Returns
        -------
        volumes : list[Volume]
            A list of the volumes in the geometry, after the requested
            modification was applied.
        features : list[Feature]
            A list of currently active features in the geometry, after the
            requested modification was applied.
        feature_issues : list[FeatureIssues]
            A list of issues that may affect the feature.
        """
        req = geometrypb.ModifyGeometryRequest(
            geometry_id=self.id,
            modification=modification,
        )
        res: geometrypb.ModifyGeometryResponse = get_default_client().ModifyGeometry(req)

        # TODO: not sure about this as the return values
        return list(res.volumes), list(res.features), list(res.features_issues)

    def check(self) -> tuple[bool, list[str]]:
        """
        Check the geometry for any issues that may prevent meshing.

        Returns
        -------
        ok : boolean
            If true, the geometry is ready for meshing.

            If false, the geometry contains errors. Inspect issues and resolve
            any errors.
        issues : list[str]
            A list of issues with the geometry.

            When ok=True, issues may be empty or non-empty but contain only
            warning or informational messages. When ok=False, issues will
            contain at least one error message and possibly additional warning
            or informational messages.
        """

        res: geometrypb.CheckGeometryResponse = get_default_client().CheckGeometry(
            geometrypb.CheckGeometryRequest(geometry_id=self.id)
        )
        return res.ok, list(res.issues)

    def list_entities(self) -> tuple[list[Surface], list[Volume]]:
        """
        List all the entities in the geometry.

        Returns
        -------
        surfaces : list[Surface]
            A list of all the surfaces in the geometry.
        volumes : list[Volume]
            A list of all the volumes in the geometry.
        """

        res: geometrypb.ListGeometryEntitiesResponse = get_default_client().ListGeometryEntities(
            geometrypb.ListGeometryEntitiesRequest(geometry_id=self.id)
        )
        surfaces = [
            Surface(
                geometry_id=self.id,
                id=f.id,
                bbox_min=Vector3(f.bbox_min.x, f.bbox_min.y, f.bbox_min.z),
                bbox_max=Vector3(f.bbox_max.x, f.bbox_max.y, f.bbox_max.z),
            )
            for f in res.faces
        ]
        volumes = [
            Volume(
                geometry_id=self.id,
                id=str(b.id),
                bbox_min=Vector3(b.bbox_min.x, b.bbox_min.y, b.bbox_min.z),
                bbox_max=Vector3(b.bbox_max.x, b.bbox_max.y, b.bbox_max.z),
            )
            for b in res.bodies
        ]
        return surfaces, volumes

    def list_features(
        self,
    ) -> list[gpb.Feature]:
        """
        List the current features in the geometry.

        Returns
        -------
        features : list[Feature]
            A list of the current features in the geometry.
        """
        req = geometrypb.ListGeometryFeaturesRequest(
            geometry_id=self.id,
        )
        res: geometrypb.ListGeometryFeaturesResponse = get_default_client().ListGeometryFeatures(
            req
        )
        return list(res.features)

    def list_feature_issues(
        self,
    ) -> list[gpb.FeatureIssues]:
        """
        List any issues with features in the geometry.

        Returns
        -------
        feature_issues : list[FeatureIssues]
            A list of any issues with features in the geometry. Issues may be
            informational, warnings or errors.
        """
        req = geometrypb.ListGeometryFeatureIssuesRequest(
            geometry_id=self.id,
        )
        res: geometrypb.ListGeometryFeatureIssuesResponse = (
            get_default_client().ListGeometryFeatureIssues(req)
        )
        return list(res.features_issues)


def get_geometry(id: str) -> Geometry:
    """
    Get a specific geometry with the given ID.

    Parameters
    ----------
    id : str
        Geometry ID.

    Returns
    -------
    Geometry
        The requested Geometry.
    """

    req = geometrypb.GetGeometryRequest(geometry_id=id)
    res: geometrypb.GetGeometryResponse = get_default_client().GetGeometry(req)
    return Geometry(res.geometry)
