"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import enum
import math

from git.index import typ

import gauge


class Type(enum.Enum):
    LINEAR = 1
    LOGARITHMIC = 2
    EXPONENTIAL = 3


class Object:
    def __init__(self) -> None:
        self.type: Type = Type.LINEAR

        self.pen: gauge.Pen = gauge.Pen()
        # Position of the scale on gauge [(-1;-1) ; (1;1)]
        self.position = (0.0, 0.0)
        # Radius of the scale main measurement line
        self.radius = 0.96
        # Rotation of the scale (CCW)
        self.rotation = 0.0
        # Span of the scale main measurement line (radians) [0; 2*pi]
        self.span = 2 * math.pi * 0.9
        # Range of the scale in measured units
        self.range = (0.0, 1.0)
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

    def from_dict(self, data) -> None:
        pass

    def set_range(self, new_val: tuple[float, float]) -> None:
        self.range = new_val
        self.maj_ticks.range = new_val
        self.maj_ticks.label_range = new_val

    def get_angle(self, val: float) -> float:
        # Clamp value to the scale range
        i_val: float = gauge.clamp(val, self.range[0], self.range[1])
        # Normalize value
        norm_val: float = gauge.normalize(i_val, self.range[0], self.range[1])
        if self.type == Type.LOGARITHMIC:
            convexity = 10.0
            new_val: float = math.log10(
                1.0 + norm_val * convexity
            ) / math.log10(1.0 + convexity)
            norm_val = new_val
        norm_val *= self.span

        return norm_val
