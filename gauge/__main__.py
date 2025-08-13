"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import math

import gauge.exporter
import gauge.round_gauge
import gauge.scale

gauge1 = gauge.round_gauge.Object()

scale1 = gauge.scale.Object()
scale1.set_range((0.0, 10.0))
scale1.maj_ticks.count = 9
gauge1.add_scale(scale1)

exporter = gauge.exporter.Object()
exporter.export(gauge1, "/tmp/gauge1.svg")


o = gauge.round_gauge.Object()
o.label.text = "Circular logarithmic ruler"
o.label.position = (-0.45, -0.2)
o.pen.color.from_fixed(gauge.FixedColor.BLACK)
o.pen.thickness = 0.005
o.size = (4096, 4096)

s = gauge.scale.Object()
s.radius = 0.8
s.font.size = 0.04
s.type = gauge.scale.Type.LOGARITHMIC
s.range = (1.0, 10.0)
s.maj_ticks.count = 8
s.label.text = "D"
s.label.position = (0.75, -0.05)
s.label.rotation = math.pi / 2.0
s.span = math.pi * 2
s.label_radius = 0.66
s.maj_shift = (-0.025, -0.03)
s.pen.thickness = 0.0025
s.maj_ticks.length = 0.1
s.maj_ticks.label_angle = math.pi / 2.0
s.maj_ticks.label_range = (1.0, 9.0)

t1 = gauge.Ticks()
t1.range = (1.0, 10.0)
t1.count = 1
t1.length = 0.08
t1.pen.thickness = 0.0035
t1.draw_labels = True
t1.label_range = (1.0, 10.0)
t1.label_font.size = 0.03
t1.label_angle = math.pi / 2.0
t1.label_prec = (1, 2)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (1.0, 10.0)
t2.count = 9
t2.length = 0.06
t2.pen.thickness = 0.0035
s.min_ticks.append(t2)

t3 = gauge.Ticks()
t3.range = (1.0, 10.0)
t3.count = 19
t3.length = 0.04
t3.pen.thickness = 0.003
s.min_ticks.append(t3)

t6 = gauge.Ticks()
t6.range = (1.0, 1.5)
t6.count = 199
t6.length = 0.01
t6.pen.thickness = 0.002
s.min_ticks.append(t6)

t4 = gauge.Ticks()
t4.range = (1.0, 3.0)
t4.count = 99
t4.length = 0.02
t4.pen.thickness = 0.0025
s.min_ticks.append(t4)

t5 = gauge.Ticks()
t5.range = (3.0, 6.0)
t5.count = 39
t5.length = 0.02
t5.pen.thickness = 0.0025
s.min_ticks.append(t5)

o.add_scale(s)

s = gauge.scale.Object()
s.radius = 0.8
s.font.size = 0.04
s.type = gauge.scale.Type.LOGARITHMIC
s.range = (1.0, 10.0)
s.maj_ticks.count = 8
s.maj_ticks.length = -0.1
s.label.text = "C"
s.label.position = (0.9, -0.05)
s.label.rotation = math.pi / 2.0
s.span = math.pi * 2
s.label_radius = 0.94
s.maj_shift = (-0.02, -0.04)
s.pen.thickness = 0.004
s.maj_ticks.label_angle = math.pi / 2.0
s.maj_ticks.label_range = (1.0, 9.0)

t1 = gauge.Ticks()
t1.range = (1.0, 10.0)
t1.count = 1
t1.length = -0.08
t1.pen.thickness = 0.0035
t1.draw_labels = True
t1.label_range = (1.0, 10.0)
t1.label_font.size = 0.03
t1.label_angle = math.pi / 2.0
t1.label_prec = (1, 2)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (1.0, 10.0)
t2.count = 9
t2.length = -0.06
t2.pen.thickness = 0.0035
s.min_ticks.append(t2)

t3 = gauge.Ticks()
t3.range = (1.0, 10.0)
t3.count = 19
t3.length = -0.04
t3.pen.thickness = 0.003
s.min_ticks.append(t3)

t6 = gauge.Ticks()
t6.range = (1.0, 1.5)
t6.count = 199
t6.length = -0.01
t6.pen.thickness = 0.002
s.min_ticks.append(t6)

t4 = gauge.Ticks()
t4.range = (1.0, 3.0)
t4.count = 99
t4.length = -0.02
t4.pen.thickness = 0.0025
s.min_ticks.append(t4)

t5 = gauge.Ticks()
t5.range = (3.0, 6.0)
t5.count = 39
t5.length = -0.02
t5.pen.thickness = 0.0025
s.min_ticks.append(t5)

o.add_scale(s)

e = gauge.exporter.Object()
e.export(o, "/tmp/ruler.svg")


o = gauge.round_gauge.Object()
o.label.text = "Pressure"
o.label.position = (-0.18, -0.2)

s = gauge.scale.Object()
s.rotation = -math.pi / 2.0 - 0.2
s.radius = 0.6
s.span = math.pi * 2.0 - 1.0
s.range = (1.0, 15.0)
s.maj_ticks.label_range = (1.0, 15.0)
s.maj_ticks.count = 13
s.maj_ticks.length = 0.08
s.label_radius = 0.45
s.label.text = "Atm."
s.label.position = (0.2, -0.41)
s.maj_ticks.label_prec = (2, 2)
s.font.size = 0.08
mt = gauge.Ticks()
mt.range = (1.0, 15.0)
mt.count = 1
mt.length = 0.05
s.min_ticks.append(mt)
o.add_scale(s)

start_val = 1.02069  # Atm
start_angle = s.get_angle(start_val)
end_val = 14.6299
end_angle = s.get_angle(end_val)

s = gauge.scale.Object()
s.rotation = -math.pi / 2.0 - 0.2 - start_angle
s.radius = 0.63
s.span = end_angle - start_angle
s.range = (15.0, 215)
s.maj_ticks.label_range = (15.0, 215)
mt = gauge.Ticks()
mt.range = (15.0, 215)
mt.count = 3
mt.shift = 0
mt.length = -0.05
s.min_ticks.append(mt)
s.maj_ticks.count = 9
s.maj_ticks.shift = 0.08
s.maj_ticks.length = 0.08
s.label_radius = 0.8
s.color = (0.4, 0.2, 0.2, 1.0)
s.label.text = "PSI"
s.label.position = (0.38, -0.51)
s.maj_ticks.label_prec = (3, 3)
s.font.size = 0.08
o.add_scale(s)

e = gauge.exporter.Object()
e.export(o, "/tmp/manometer.svg")


o = gauge.round_gauge.Object()

s = gauge.scale.Object()
s.rotation = math.pi / 2.0
s.radius = 0.9
s.span = math.pi * 2.0
s.range = (0.0, 12.0)

mt = gauge.Ticks()
mt.count = 4
mt.length = 0.04
mt.range = (0.0, 12.0)
s.min_ticks.append(mt)

s.maj_ticks.count = 11
s.maj_ticks.length = 0.08
s.maj_ticks.label_range = (1.0, 12.0)
s.maj_ticks.label_prec = (1, 2)
s.font.size = 0.15
s.font.face = gauge.FontFace.SANS
s.label_radius = 0.7
o.add_scale(s)

e.export(o, "/tmp/clock.svg")


o = gauge.round_gauge.Object()

s = gauge.scale.Object()
s.rotation = math.pi / 2.0
s.radius = 0.95
s.span = math.pi * 2.0
s.range = (0.0, 24.0)

mt = gauge.Ticks()
mt.count = 1
mt.length = 0.06
mt.range = (0.0, 24.0)
s.min_ticks.append(mt)

mt = gauge.Ticks()
mt.count = 4
mt.length = 0.03
mt.range = (0.0, 24.0)
s.min_ticks.append(mt)

s.maj_ticks.count = 11
s.maj_ticks.length = 0.1
s.maj_ticks.label_range = (1.0, 24.0)
s.maj_ticks.label_prec = (1, 2)
s.font.size = 0.12
s.font.face = gauge.FontFace.SANS
s.label_radius = 0.74
o.add_scale(s)

s = gauge.scale.Object()
s.rotation = math.pi / 2.0
s.position = (0, -0.3)
s.radius = 0.32
s.span = math.pi * 2.0
s.range = (0.0, 60.0)
s.font.size = 0.06
mt = gauge.Ticks()
mt.count = 4
mt.length = 0.02
s.min_ticks.append(mt)
s.maj_ticks.count = 12
s.maj_ticks.length = 0.04
s.label_radius = 0.23
s.maj_shift = (-0.03, -0.02)
o.add_scale(s)

e.export(o, "/tmp/tank_clock.svg")


"""
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

o = gauge.round_gauge.Object()
o.size = (400, 400)
s = gauge.scale.Object()
s.type = gauge.scale.Type.LOGARITHMIC
s.range = (0, 1.0e10)
s.maj_ticks.count = 9
s.radius = 0.8
s.label_radius = 0.6
s.font.size = 0.05
s.maj_shift = (-0.05, -0.025)
o.scales.append(s)
e.export(o, "/tmp/4.svg")
"""
