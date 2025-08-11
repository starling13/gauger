"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import gauge
import gauge.scale


class Object:
    def __init__(self) -> None:
        self.pen: gauge.Pen = gauge.Pen()
        self.radius: float = 0.98
        self.scales: list[gauge.scale.Object] = []
        self.size: tuple[int, int] = (800, 800)
        self.label: gauge.Label = gauge.Label()

    def from_dict(self, data) -> None:
        gauge_o = data.get("gauge")
        if gauge_o is None:
            raise Exception("No 'gauge' object")

        size_o = gauge_o.get("size")
        if size_o is None:
            raise Exception("No 'size' field in 'gauge' object")

        if (
            (not isinstance(size_o, list))
            or len(size_o) != 2
            or (not all(isinstance(x, int) for x in size_o))
        ):
            raise Exception(
                "The 'size' field in 'gauge' object is not a tuple of 2 integer values"
            )

        self.size = (size_o[0], size_o[1])

        radius_o = gauge_o.get("radius")
        if radius_o is None:
            raise Exception("No 'radius' field in 'gauge' object")

        if not isinstance(radius_o, float):
            raise Exception(
                "The 'radius' field in 'gauge' object is not float value"
            )
        self.radius = radius_o
