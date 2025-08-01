"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import gauge
import gauge.scale


class Object:
    def __init__(self) -> None:
        self.border_width: float = 0.02
        self.radius: float = 0.98
        self.scales: list[gauge.scale.Object] = []
        self.label: gauge.Label = gauge.Label()
