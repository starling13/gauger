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
s.maj_ticks.count = 14
s.maj_ticks.length = 0.08
s.label_radius = 0.45
s.label.text = "Atm."
s.label.position = (0.2, -0.42)
s.maj_prec = (2, 0)
s.maj_shift = (-0.05, -0.03)
s.font.size = 0.08
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
s.min_ticks.count = 3
s.min_ticks.shift = 0.04
s.min_ticks.length = 0.04
s.maj_ticks.count = 10
s.maj_ticks.shift = 0.08
s.maj_ticks.length = 0.08
s.label_radius = 0.8
s.color = (0.4, 0.2, 0.2, 1.0)
s.label.text = "PSI"
s.label.position = (0.34, -0.51)
s.maj_prec = (3, 0)
s.maj_shift = (-0.05, -0.03)
s.font.size = 0.08
o.scales.append(s)

e = gauge.exporter.Object()
e.export(o, "/tmp/2.svg")

o = gauge.round_gauge.Object()

s = gauge.scale.Object()
s.rotation = math.pi / 2.0
s.radius = 0.9
s.span = math.pi * 2.0
s.range = (0.0, 12.0)
s.min_ticks.count = 4
s.min_ticks.length = 0.04
s.maj_ticks.count = 12
s.maj_ticks.length = 0.08
s.maj_ticks_start = 1
s.font.size = 0.2
s.font.face = gauge.FontFace.SANS
s.label_radius = 0.7
s.maj_prec = (2, 0)
s.maj_shift = (-0.11, -0.07)
o.scales.append(s)

s = gauge.scale.Object()
s.rotation = math.pi / 2.0
s.position = (0, -0.3)
s.radius = 0.32
s.span = math.pi * 2.0
s.range = (0.0, 60.0)
s.font.size = 0.06
s.min_ticks.count = 4
s.min_ticks.length = 0.02
s.maj_ticks.count = 12
s.maj_ticks.length = 0.04
s.maj_ticks_start = 1
s.label_radius = 0.23
s.maj_prec = (2, 0)
s.maj_shift = (-0.03, -0.02)
o.scales.append(s)

e.export(o, "/tmp/3.svg")

o = gauge.round_gauge.Object()
o.size = (400, 400)

s = gauge.scale.Object()
# Range of the angles in degrees [0; 360]
s.range = (0.0, 360.0)
# Radius of the scale line
s.radius = 0.92
# Radius of the scale labels line
s.label_radius = 0.82
# Rotation of the scale
s.rotation = math.pi / 2.0
# Major ticks parameters
s.maj_ticks.count = 24
s.maj_ticks.length = 0.04
s.maj_ticks_start = 1

s.span = math.pi * 2.0
s.min_ticks.count = 2
s.min_ticks.length = 0.02
s.maj_shift = (-0.05, -0.015)
s.font.size = 0.05

o.scales.append(s)
e.export(o, "/tmp/1.svg")
