# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Test script
"""

import math

import gauge.exporter
import gauge.round_gauge
import gauge.scale

exporter = gauge.exporter.Object()

"""
o = gauge.round_gauge.Object()
o.label.text = "Circular slide rule"
o.label.position = (-0.3, -0.1)
o.label.font.set_size(0.075)
o.pen.color.from_fixed(gauge.FixedColor.BLACK)
o.pen.thickness = 0.005
o.size = (4096, 4096)
o.pen.thickness = 0.0025

s = gauge.scale.Object()
o.add_scale(s)
s.radius = 0.82
s.pen.thickness = 0.0025
s.font.set_size(0.05)
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.range = (1.0, 10.0)
s.label.text = "C"
s.label.position = (0.77, -0.07)
s.label.rotation = math.pi / 2.0
s.label.font.set_size(0.075)
s.span = math.pi * 2
s.label_radius = 0.71
s.maj_shift = (0.0, 0.0)
s.maj_ticks.pen.thickness = 0.005
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.06)
s.maj_ticks.length = 0.08
s.maj_ticks.label_prec = (0, 1)
s.maj_ticks.label_angle = math.pi / 2.0
s.maj_ticks.label_range = (1.0, 9.0)

t1 = gauge.Ticks()
s.min_ticks.append(t1)
t1.range = (1.0, 10.0)
t1.count = 1
t1.length = 0.06
t1.pen.thickness = 0.003
t1.draw_labels = True
t1.label_range = (1.0, 10.0)
t1.label_font.set_size(0.03)
t1.label_angle = math.pi / 2.0
t1.label_prec = (1, 2)


t2 = gauge.Ticks()
t2.range = (1.0, 10.0)
t2.count = 9
t2.length = 0.06
t2.pen.thickness = 0.0025
s.min_ticks.append(t2)


t3 = gauge.Ticks()
t3.range = (1.0, 10.0)
t3.count = 19
t3.length = 0.05
t3.pen.thickness = 0.002
s.min_ticks.append(t3)

t6 = gauge.Ticks()
t6.range = (1.0, 1.5)
t6.count = 199
t6.length = 0.03
t6.pen.thickness = 0.001
s.min_ticks.append(t6)

t4 = gauge.Ticks()
t4.range = (1.0, 3.0)
t4.count = 99
t4.length = 0.04
t4.pen.thickness = 0.0015
s.min_ticks.append(t4)

t5 = gauge.Ticks()
t5.range = (3.0, 6.0)
t5.count = 39
t5.length = 0.04
t5.pen.thickness = 0.0015
s.min_ticks.append(t5)

s = gauge.scale.Object()
o.add_scale(s)
s.radius = 0.82
s.pen.thickness = 0.0025
s.font.set_size(0.03)
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.range = (1.0, 10.0)
s.maj_ticks.count = 9
s.maj_ticks.length = -0.09
s.label.text = "D"
s.label.font.set_size(0.075)
s.label.position = (0.91, -0.07)
s.label.rotation = math.pi / 2.0
s.span = math.pi * 2
s.label_radius = 0.94
s.maj_ticks.pen.thickness = 0.0035
s.maj_ticks.label_prec = (0, 1)
s.maj_ticks.label_font.set_size(0.07)
s.maj_ticks.label_angle = math.pi / 2.0
s.maj_ticks.label_range = (1.0, 9.0)

t1 = gauge.Ticks()
t1.range = (1.0, 10.0)
t1.count = 1
t1.length = -0.07
t1.pen.thickness = 0.003
t1.draw_labels = True
t1.label_range = (1.0, 10.0)
t1.label_font.set_size(0.03)
t1.label_angle = math.pi / 2.0
t1.label_prec = (1, 2)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (1.0, 10.0)
t2.count = 9
t2.length = -0.06
t2.pen.thickness = 0.0025
s.min_ticks.append(t2)

t3 = gauge.Ticks()
t3.range = (1.0, 10.0)
t3.count = 19
t3.length = -0.05
t3.pen.thickness = 0.002
s.min_ticks.append(t3)

t6 = gauge.Ticks()
t6.range = (1.0, 1.5)
t6.count = 199
t6.length = -0.03
t6.pen.thickness = 0.001
s.min_ticks.append(t6)

t4 = gauge.Ticks()
t4.range = (1.0, 3.0)
t4.count = 99
t4.length = -0.04
t4.pen.thickness = 0.0015
s.min_ticks.append(t4)

t5 = gauge.Ticks()
t5.range = (3.0, 6.0)
t5.count = 39
t5.length = -0.04
t5.pen.thickness = 0.0015
s.min_ticks.append(t5)

s = gauge.scale.Object()
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.set_range(1.0, 10.0)
s.radius = 0.665
s.pen.thickness = 0.0025
s.label.text = "A"
s.label.position = (0.6, -0.07)
s.label.font.set_size(0.075)
s.label.rotation = math.pi / 2.0
s.maj_ticks.pen.thickness = 0.004
s.span = math.pi
s.font.set_size(0.04)
s.label_radius = 0.55
s.maj_ticks.length = 0.09
s.maj_ticks.label_range = (1.0, 10.0)
s.maj_ticks.label_prec = (0, 2)
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.05)
s.maj_ticks.label_angle = math.pi / 2.0

t1 = gauge.Ticks()
t1.range = (1.0, 10.0)
t1.count = 1
t1.length = 0.07
t1.pen.thickness = 0.003
t1.draw_labels = True
t1.label_range = (1.0, 7.5)
t1.label_font.set_size(0.03)
t1.label_angle = math.pi / 2.0
t1.label_prec = (1, 2)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (1.0, 10.0)
t2.count = 9
t2.length = 0.06
t2.pen.thickness = 0.002
s.min_ticks.append(t2)

t4 = gauge.Ticks()
t4.range = (1.0, 3.0)
t4.count = 49
t4.length = 0.04
t4.pen.thickness = 0.0015
s.min_ticks.append(t4)

t3 = gauge.Ticks()
t3.range = (3.0, 6.0)
t3.count = 19
t3.length = 0.04
t3.pen.thickness = 0.0025
s.min_ticks.append(t3)

o.add_scale(s)

s = gauge.scale.Object()
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.set_range(10.0, 100.0)
s.radius = 0.665
s.pen.thickness = 0.0025
s.label.text = ""  # A
s.maj_ticks.pen.thickness = 0.004
s.span = math.pi
s.rotation = math.pi
s.font.set_size(0.04)
s.label_radius = 0.55
s.maj_ticks.length = 0.09
s.maj_ticks.label_range = (20.0, 90.0)
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.05)
s.maj_ticks.label_angle = math.pi / 2.0

t1 = gauge.Ticks()
t1.range = (10.0, 100.0)
t1.count = 1
t1.length = 0.07
t1.pen.thickness = 0.003
t1.draw_labels = True
t1.label_range = (10.0, 75.0)
t1.label_font.set_size(0.03)
t1.label_angle = math.pi / 2.0
t1.label_prec = (2, 2)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (10.0, 100.0)
t2.count = 9
t2.length = 0.06
t2.pen.thickness = 0.002
s.min_ticks.append(t2)

t4 = gauge.Ticks()
t4.range = (10.0, 30.0)
t4.count = 49
t4.length = 0.04
t4.pen.thickness = 0.0015
s.min_ticks.append(t4)

t3 = gauge.Ticks()
t3.range = (30.0, 60.0)
t3.count = 19
t3.length = 0.04
t3.pen.thickness = 0.0025
s.min_ticks.append(t3)

o.add_scale(s)

s = gauge.scale.Object()
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.set_range(1.0, 10.0)
s.radius = 0.52
s.pen.thickness = 0.0025
s.label.text = "K"
s.label.position = (0.45, -0.07)
s.label.font.set_size(0.075)
s.label.rotation = math.pi / 2.0
s.maj_ticks.pen.thickness = 0.003
s.span = 2.0 / 3.0 * math.pi
s.font.set_size(0.04)
s.label_radius = 0.4
s.maj_ticks.length = 0.09
s.maj_ticks.label_range = (1.0, 9.0)
s.maj_ticks.label_prec = (0, 2)
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.04)
s.maj_ticks.label_angle = math.pi / 2.0

quit(0)
t1 = gauge.Ticks()
t1.range = (1.0, 10.0)
t1.count = 1
t1.length = 0.07
t1.pen.thickness = 0.003
t1.draw_labels = True
t1.label_range = (1.0, 4.0)
t1.label_font.set_size(0.03)
t1.label_angle = math.pi / 2.0
t1.label_prec = (1, 2)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (1.0, 6.0)
t2.count = 9
t2.length = 0.06
t2.pen.thickness = 0.0015
s.min_ticks.append(t2)

t7 = gauge.Ticks()
t7.range = (1.0, 3.0)
t7.count = 19
t7.length = 0.04
t7.pen.thickness = 0.001
s.min_ticks.append(t7)

t3 = gauge.Ticks()
t3.range = (6.0, 10.0)
t3.count = 3
t3.length = 0.06
t3.pen.thickness = 0.001
s.min_ticks.append(t3)

o.add_scale(s)

s = gauge.scale.Object()
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.set_range(10.0, 100.0)
s.radius = 0.52
s.pen.thickness = 0.0025
s.label.text = ""  # K2
s.label.position = (0.4, -0.05)
s.label.rotation = math.pi / 2.0
s.maj_ticks.pen.thickness = 0.003
s.rotation = 2.0 / 3.0 * math.pi
s.span = 2.0 / 3.0 * math.pi
s.font.set_size(0.04)
s.label_radius = 0.4
s.maj_ticks.length = 0.09
s.maj_ticks.label_range = (10.0, 80.0)
s.maj_ticks.label_prec = (0, 2)
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.04)
s.maj_ticks.label_angle = math.pi / 2.0

t1 = gauge.Ticks()
t1.range = (10.0, 100.0)
t1.count = 1
t1.length = 0.07
t1.pen.thickness = 0.002
t1.draw_labels = True
t1.label_range = (10.0, 30.0)
t1.label_font.set_size(0.03)
t1.label_angle = math.pi / 2.0
t1.label_prec = (2, 3)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (10.0, 60.0)
t2.count = 9
t2.length = 0.06
t2.pen.thickness = 0.001
s.min_ticks.append(t2)

t7 = gauge.Ticks()
t7.range = (10.0, 30.0)
t7.count = 19
t7.length = 0.04
t7.pen.thickness = 0.001
s.min_ticks.append(t7)

t3 = gauge.Ticks()
t3.range = (60.0, 100.0)
t3.count = 3
t3.length = 0.06
t3.pen.thickness = 0.001
s.min_ticks.append(t3)

o.add_scale(s)

s = gauge.scale.Object()
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.set_range(100.0, 1000.0)
s.radius = 0.52
s.pen.thickness = 0.0025
s.label.text = ""  # K3
s.label.position = (0.4, -0.05)
s.label.rotation = math.pi / 2.0
s.maj_ticks.pen.thickness = 0.003
s.rotation = 4.0 / 3.0 * math.pi
s.span = 2.0 / 3.0 * math.pi
s.font.set_size(0.04)
s.label_radius = 0.4
s.maj_ticks.length = 0.09
s.maj_ticks.label_range = (100.0, 600.0)
s.maj_ticks.label_prec = (3, 3)
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.04)
s.maj_ticks.label_angle = math.pi / 2.0

t1 = gauge.Ticks()
t1.range = (100.0, 1000.0)
t1.count = 1
t1.length = 0.07
t1.pen.thickness = 0.002
t1.draw_labels = True
t1.label_range = (100.0, 200.0)
t1.label_font.set_size(0.03)
t1.label_angle = math.pi / 2.0
t1.label_prec = (3, 3)
s.min_ticks.append(t1)

t2 = gauge.Ticks()
t2.range = (100.0, 600.0)
t2.count = 9
t2.length = 0.06
t2.pen.thickness = 0.001
s.min_ticks.append(t2)

t3 = gauge.Ticks()
t3.range = (600.0, 1000.0)
t3.count = 3
t3.length = 0.06
t3.pen.thickness = 0.001
s.min_ticks.append(t3)

t7 = gauge.Ticks()
t7.range = (100.0, 300.0)
t7.count = 19
t7.length = 0.04
t7.pen.thickness = 0.001
s.min_ticks.append(t7)

o.add_scale(s)

e = gauge.exporter.Object()
e.export(o, "/tmp/ruler2.svg")
"""

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
"""
