"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import math

import gauge.exporter
import gauge.round_gauge
import gauge.scale

o = gauge.round_gauge.Object()
o.label.text = "Pressure"
o.label.position = (-0.18, -0.2)

s = gauge.scale.Object()
s.rotation = -math.pi / 2.0 - 0.2
s.radius = 0.6
s.span = math.pi * 2.0 - 1.0
s.range = (1.0, 15.0)
s.maj_ticks = 14
s.label_radius = 0.45
s.tick_len = 0.08
s.label.text = "Atm."
s.label.position = (0.2, -0.42)
s.maj_prec = (2, 0)
s.maj_shift = (-0.05, 0.03)
o.scales.append(s)

start_val = 1.02069  # Atm
start_angle = s.get_angle(start_val)
end_val = 14.6299
end_angle = s.get_angle(end_val)

s = gauge.scale.Object()
s.rotation = -math.pi / 2.0 - 0.2 - start_angle
s.radius = 0.63
s.span = end_angle - start_angle
s.range = (15.0, 215)
s.maj_ticks = 10
s.label_radius = 0.8
s.tick_len = -0.08
s.color = (0.4, 0.2, 0.2, 1.0)
s.label.text = "PSI"
s.label.position = (0.34, -0.51)
s.maj_prec = (4, 1)
s.maj_shift = (-0.08, 0.03)
o.scales.append(s)

e = gauge.exporter.Object()
e.export(o, "/tmp/2.svg")

o = gauge.round_gauge.Object()
s = gauge.scale.Object()
s.rotation = 0.0
s.radius = 0.8
s.span = math.pi * 2.0
s.range = (0.0, 12.0)
s.maj_ticks = 12
s.label_radius = 0.6
s.tick_len = 0.08
s.maj_prec = (2, 0)
s.maj_shift = (-0.05, 0.03)
o.scales.append(s)
e.export(o, "/tmp/3.svg")
