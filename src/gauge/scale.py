# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Module of the scale class
"""

import enum
import logging
import math

import gauge


class Type(enum.Enum):
    """
    @brief Scale type
    """

    LINEAR = 1
    LOGARITHMIC = 2
    EXPONENTIAL = 3


class ScaleSector:
    def __init__(self) -> None:
        self.range: tuple[float, float] = (0.0, 0.0)
        self.color: gauge.Color = gauge.Color.create_from_fixed(gauge.FixedColor.CYAN)
        self.radius_range: tuple[float, float] = (0.0, 0.0)


class Object:
    def __init__(self) -> None:
        # Type of the scale
        self.__type: Type = Type.LINEAR
        # Pen for the scale
        self.pen: gauge.Pen = gauge.Pen()
        # Position of the scale on gauge [(-1;-1) ; (1;1)]
        self.position = (0.0, 0.0)
        # Radius of the scale main measurement line
        self.radius = 0.96
        # Rotation of the scale (CCW)
        self.rotation = 0.0
        # Span of the scale main measurement line (radians) [0; 2*pi]
        self.span = 2 * math.pi * 0.9
        # Scale narrowing
        self.narrowing = math.nan
        # Range of the scale in measured units
        self.__range = (0.0, 1.0)
        # Minor ticks count
        self.min_ticks: list[gauge.Ticks] = []
        # Major ticks count
        self.maj_ticks = gauge.Ticks()
        # Font for labels
        self.font = gauge.Font()
        #
        self.maj_shift = (0.0, 0.0)
        #
        self.label_radius = 0.7
        #
        self.color = (0.0, 0.0, 0.0, 1.0)
        #
        self.label: gauge.Label = gauge.Label()

        self.__sectors: list[ScaleSector] = []

    def add_sector(self, sector: ScaleSector) -> None:
        self.__sectors.append(sector)

    @property
    def sectors(self) -> list[ScaleSector]:
        return self.__sectors

    @property
    def type(self) -> Type:
        return self.__type

    def set_type(self, new_val: Type) -> None:
        self.__type = new_val

    @property
    def range(self) -> tuple[float, float]:
        return self.__range

    @range.setter
    def range(self, new_val: tuple[float, float]) -> None:
        self.__range = new_val
        self.maj_ticks.range = new_val
        self.maj_ticks.label_range = new_val

    def add_minor_ticks(self, ticks: gauge.Ticks) -> None:
        self.min_ticks.append(ticks)
        ticks.range = self.range

    def from_dict(self, data) -> None:
        # Range property
        range_o = data.get("range")
        if range_o is None:
            logging.warning("No 'range' field in 'scale' object")
        else:
            if (
                (not isinstance(range_o, list))
                or len(range_o) != 2
                or (not all(isinstance(x, float) for x in range_o))
            ):
                raise Exception(
                    "The 'range' field in 'scale' object is not a "
                    "tuple of 2 real values"
                )
            self.range = (range_o[0], range_o[1])

        # Radius property
        radius_o = data.get("radius")
        if radius_o is None:
            logging.warning("No 'radius' field in 'scale' object")
        else:
            if not isinstance(radius_o, float):
                raise ValueError(
                    "The 'radius' field in 'scale' object is not a real value"
                )
            self.radius = radius_o

        # Rotation property
        rot_o = data.get("rotation")
        if rot_o is None:
            logging.warning("No 'rotation' field in 'scale' object")
        else:
            if not isinstance(rot_o, float):
                raise Exception(
                    "The 'rotation' field in 'scale' object is not a " "real value"
                )
            self.rotation = math.radians(rot_o)

        # Span property
        span_o = data.get("span")
        if span_o is None:
            logging.warning("No 'span' field in 'scale' object")
        else:
            if not isinstance(span_o, float):
                raise Exception(
                    "The 'span' field in 'scale' object is not a " "real value"
                )
            self.span = math.radians(span_o)

        # Major ticks object
        maj_ticks_o = data.get("maj_ticks")
        if maj_ticks_o is None:
            logging.warning("No 'maj_ticks' object in 'scale' object")
        else:
            self.maj_ticks.from_dict(maj_ticks_o)

        # Minor ticks list
        min_ticks_o = data.get("min_ticks")
        if min_ticks_o is None:
            logging.warning("No 'min_ticks' list in 'scale' object")
        else:
            if not isinstance(min_ticks_o, dict):
                raise Exception(
                    "The 'min_ticks' field in 'scale' object " "is not a dictionary"
                )
            for k, v in min_ticks_o.items():
                mt = gauge.Ticks()
                mt.from_dict(v)
                self.add_minor_ticks(ticks=mt)

        # Label object
        label_o = data.get("label")
        if label_o is None:
            logging.warning("No 'label' property in 'scale' object")
        else:
            label = gauge.Label()
            label.from_dict(label_o)
            self.label = label

    def get_angle(self, val: float) -> float:
        # Clamp value to the scale range
        i_val: float = gauge.clamp(
            val,
            min(self.range[0], self.range[1]),
            max(self.range[0], self.range[1]),
        )
        # Normalize value
        norm_val: float = gauge.normalize(i_val, self.range[0], self.range[1])
        if self.type == Type.LOGARITHMIC:
            convexity = 9.0
            new_val: float = math.log10(1.0 + norm_val * convexity) / math.log10(
                1.0 + convexity
            )
            norm_val = new_val
        norm_val *= self.span

        return norm_val
