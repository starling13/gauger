"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import math

import gauge


class Object:
    def __init__(self) -> None:
        # Position of the scale on gauge [(-1;-1) ; (1;1)]
        self.position = (0.0, 0.0)
        # Radius of the scale main measurement line
        self.radius = 0.96
        # Thickness of the scale main measurement line
        self.line = 0.01
        # Rotation of the scale (CCW)
        self.rotation = 0.0
        # Span of the scale main measurement line (radians) [0; 2*pi]
        self.span = 2 * math.pi * 0.9
        # Range of the scale in measured units
        self.range = (0.0, 1.0)
        # Minor ticks count
        self.min_ticks = gauge.Ticks()
        # Major ticks count
        self.maj_ticks = gauge.Ticks()
        self.font = gauge.Font()
        #
        self.maj_prec = (2, 1)
        #
        self.maj_shift = (0.0, 0.0)
        #
        self.maj_ticks_start = 0
        #
        self.label_radius = 0.7
        #
        self.color = (0.0, 0.0, 0.0, 1.0)
        #
        self.label: gauge.Label = gauge.Label()

    def get_angle(self, val: float) -> float:
        values_span = self.range[1] - self.range[0]
        return self.span * (val - self.range[0]) / values_span
