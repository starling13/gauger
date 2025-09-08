# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Module of the round gauge class
"""

import logging

import gauge
import gauge.scale


class Object:
    def __init__(self) -> None:
        self.pen: gauge.Pen = gauge.Pen()
        self.radius: float = 0.98
        self.scales: list[gauge.scale.Object] = []
        self.size: tuple[int, int] = (800, 800)
        self.label: gauge.Label = gauge.Label()

    def add_scale(self, scale_object: gauge.scale.Object) -> None:
        self.scales.append(scale_object)

    def from_dict(self, data) -> None:
        size_o = data.get("size")
        if size_o is None:
            logging.warning("No 'size' field in 'gauge' object")
        else:
            if (
                (not isinstance(size_o, list))
                or len(size_o) != 2
                or (not all(isinstance(x, int) for x in size_o))
            ):
                raise Exception(
                    "The 'size' field in 'gauge' object is not a tuple of 2 integer values"
                )
            self.size = (size_o[0], size_o[1])

        radius_o = data.get("radius")
        if radius_o is None:
            logging.warning("No 'radius' field in 'gauge' object")
        else:
            if not isinstance(radius_o, float):
                raise Exception(
                    "The 'radius' field in 'gauge' object is not float value"
                )
            self.radius = radius_o

        scales_o = data.get("scales")
        if scales_o is None:
            logging.warning("No 'scales' field in 'gauge' object")
        else:
            for s, v in scales_o.items():
                scale_o = gauge.scale.Object()
                self.add_scale(scale_o)
                if v is not None:
                    scale_o.from_dict(v)
                else:
                    logging.warning("Empty 'scale' object")
