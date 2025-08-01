"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import math

import gauge


class Object:
    def __init__(self) -> None:
        self.position = (0.0, 0.0)
        self.radius = 0.96
        self.line = 0.01
        self.rotation = 0.0
        self.span = 2 * math.pi
        self.range = (0.0, 1.0)
        self.min_ticks = 10
        self.maj_ticks = 10
        self.tick_len = 0.2
        self.label_radius = 0.7
        self.color = (0.0, 0.0, 0.0, 1.0)
        self.label: gauge.Label = gauge.Label()

    def get_angle(self, val: float) -> float:
        values_span = self.range[1] - self.range[0]
        return self.span * (val - self.range[0]) / values_span
