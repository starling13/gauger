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
Naval astrolabe
"""

sq_gauge = gauge.round_gauge.Object()
sq_gauge.size = (1024, 1024)
sq_gauge.set_radius(0.99)

s = gauge.scale.Object()
sq_gauge.add_scale(s)
s.rotation = math.pi
s.radius = 0.99

s.set_range(180.0, -180.0)
s.span = math.pi * 2.0
s.label_radius = 0.9
s.maj_ticks.pen.thickness = 0.006
s.maj_ticks.length = 0.06
s.maj_ticks.label_font.set_size(0.05)
s.maj_ticks.label_angle = 3.0 * math.pi / 2.0
s.maj_ticks.label_prec = (0, 3)
s.maj_ticks.count = 36
s.maj_ticks.label_range = (-170.0, 180.0)

mt1 = gauge.Ticks()
s.add_minor_ticks(ticks=mt1)
mt1.count = 9
mt1.length = 0.045
mt1.pen.thickness = 0.004

mt2 = gauge.Ticks()
s.add_minor_ticks(ticks=mt2)
mt2.count = 19
mt2.length = 0.03
mt2.pen.thickness = 0.003

exporter.export(obj=sq_gauge, file_path="/tmp/naval_astrolabe.svg")


"""
Spiral scale
"""

sq_gauge = gauge.round_gauge.Object()

scale1 = gauge.scale.Object()
scale1.rotation = -0.3
scale1.set_range(1, 3000)
scale1.maj_ticks.count = 20
scale1.maj_ticks.label_font.set_size(0.05)
scale1.label_radius = 0.8
scale1.span = 20.0
scale1.narrowing = 0.035
scale1.maj_ticks.label_angle = math.pi / 2.0

sq_gauge.add_scale(scale1)

exporter.export(obj=sq_gauge, file_path="/tmp/sq_gauge.svg")

"""
"""

gauge1 = gauge.round_gauge.Object()

scale1 = gauge.scale.Object()
gauge1.add_scale(scale_object=scale1)
scale1.set_range(min_val=0.0, max_val=10.0)
scale1.maj_ticks.count = 10

mt1 = gauge.Ticks()
scale1.add_minor_ticks(ticks=mt1)
mt1.count = 1

exporter = gauge.exporter.Object()
exporter.export(obj=gauge1, file_path="/tmp/gauge1.svg")

o = gauge.round_gauge.Object()
o.label.text = "Circular slide rule"
o.label.position = (-0.3, -0.1)
o.label.font.set_size(0.075)
o.pen.color.from_fixed(gauge.FixedColor.BLACK)
o.pen.thickness = 0.005
o.size = (4096, 4096)

s = gauge.scale.Object()
o.add_scale(s)
s.radius = 0.82
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
o = gauge.round_gauge.Object()
o.label.text = "Pressure"
o.label.position = (-0.18, -0.2)

s = gauge.scale.Object()
s.rotation = -math.pi / 2.0 - 0.2
s.radius = 0.6
s.span = math.pi * 2.0 - 1.0
s.range = (1.0, 15.0)
s.maj_ticks.label_range = (1.0, 15.0)
s.maj_ticks.count = 14
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
s.maj_ticks.count = 10
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
"""

o = gauge.round_gauge.Object()

s = gauge.scale.Object()
o.add_scale(s)

s.rotation = -math.pi / 2.0
s.radius = 0.9
s.span = math.pi * 2.0
s.set_range(min_val=0.0, max_val=12.0)
s.maj_ticks.count = 12
s.maj_ticks.length = 0.1
s.maj_ticks.label_range = (1.0, 12.0)
s.maj_ticks.label_prec = (1, 2)
s.maj_ticks.label_font.set_size(0.15)
s.maj_ticks.label_font.set_face(gauge.FontFace.SANS)
s.label.text = "Toy clock"
s.label.position = (-0.25, -0.5)
s.label.font.set_face(gauge.FontFace.SERIF)
mt = gauge.Ticks()
s.add_minor_ticks(ticks=mt)
mt.count = 4
mt.length = 0.05
# mt.range = (0.0, 12.0)

e = gauge.exporter.Object()
e.export(o, "/tmp/clock.svg")


# Main object for gauge
o = gauge.round_gauge.Object()

# Main 24-hour scale of the clock
s = gauge.scale.Object()
# Add scale object to gauge before any other actions
# because it changes some properties of the scale
o.add_scale(scale_object=s)
# Rotate 90 deg CCW to orient 12 hour tick up
s.rotation = -math.pi / 2.0
# Scale has a radius of 0.95 of image half
s.radius = 0.95
# Scale span is 360 deg - full circle
s.span = math.pi * 2.0
# Setting the range of the clock [1; 24] hours, (real numbers used!).
s.set_range(min_val=0.0, max_val=24.0)
# Major tick and digit label on every 2 hours
s.maj_ticks.count = 12
# Major ticks length is ~ 0.1 of the gauge radius
s.maj_ticks.length = 0.1
# Major ticks span range from 1 to 24, excluding 0 which has 24 mark as scale spans whole 360 deg. circle.
s.maj_ticks.label_range = (1.0, 24.0)
# Set precision of the hour digit labels: minimum 1 symbol, not longer then 2
s.maj_ticks.label_prec = (1, 2)
# Relative size of the hour labels font
s.maj_ticks.label_font.set_size(0.11)
# Face of the hour labels font
s.maj_ticks.label_font.set_face(gauge.FontFace.SANS)
# Set radius of the virtual circle along which labels are placed
s.label_radius = 0.75

# Common label of the scale
s.label.text = "Tank clock"
# Common label position
s.label.position = (-0.3, 0.4)
# Font face for common label
s.label.font.set_face(gauge.FontFace.MONO)

# Minor ticks object
mt = gauge.Ticks()
# First of all add it to the scale
s.add_minor_ticks(ticks=mt)
# 1 ticks between 2 hours for odd hours
mt.count = 1
# Minor ticks are shorter then major
mt.length = 0.06
# Draw labels on minor ticks
mt.draw_labels = True
# Font size of the minor ticks is slighter smaller the in major ones
mt.label_font.set_size(0.075)
# Minor ticks span range from 0 to 24, so to add mark on 1 hour
mt.label_range = (0.0, 24.0)
# Set precision of the hour digit labels: minimum 1 symbol, not longer then 2
mt.label_prec = (1, 2)

# mt = gauge.Ticks()
# mt.count = 4
# mt.length = 0.03
# mt.range = (0.0, 24.0)
# s.min_ticks.append(mt)

"""
s = gauge.scale.Object()
s.rotation = math.pi / 2.0
s.position = (0, -0.3)
s.radius = 0.33
s.span = math.pi * 2.0
s.set_range(0.0, 60.0)
mt = gauge.Ticks()
mt.count = 4
mt.length = 0.02
mt.range = (0.0, 60.0)
s.min_ticks.append(mt)
s.maj_ticks.count = 12
s.maj_ticks.length = 0.04
s.maj_ticks.label_font.size = 0.02
s.label_radius = 0.23
s.maj_shift = (-0.03, -0.02)
o.add_scale(s)
"""

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
"""

o = gauge.round_gauge.Object()
o.size = (400, 400)
s = gauge.scale.Object()
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.range = (0, 1.0e10)
s.maj_ticks.count = 9
s.radius = 0.8
s.label_radius = 0.6
s.font.set_size(0.05)
s.maj_shift = (-0.05, -0.025)
o.scales.append(s)
e.export(o, "/tmp/4.svg")


o = gauge.round_gauge.Object()
o.label.text = "Логарифмический умножитель"
o.label.position = (-0.45, -0.1)
o.label.font.set_size(0.065)
o.pen.color.from_fixed(gauge.FixedColor.BLACK)
o.pen.thickness = 0.005
o.size = (4096, 4096)

s = gauge.scale.Object()
o.add_scale(s)
s.radius = 0.7
s.font.set_size(0.08)
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.range = (1.0, 10.0)
s.label.text = "C"
s.label.position = (0.67, -0.1)
s.label.rotation = math.pi / 2.0
s.span = math.pi
s.label_radius = 0.55
s.maj_shift = (0.0, 0.0)
s.maj_ticks.pen.thickness = 0.003
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.07)
s.maj_ticks.length = 0.08
s.maj_ticks.label_prec = (0, 1)
s.maj_ticks.label_angle = math.pi / 4.0
s.maj_ticks.label_range = (1.0, 9.0)

s = gauge.scale.Object()
o.add_scale(s)
s.radius = 0.7
s.font.set_size(0.05)
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.range = (10.0, 100.0)
s.label.text = ""  # C2
s.label.position = (0.0, 0.0)
s.label.rotation = math.pi
s.span = math.pi
s.rotation = math.pi
s.label_radius = 0.55
s.maj_shift = (0.0, 0.0)
s.pen.thickness = 0.006
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.07)
s.maj_ticks.length = 0.08
s.maj_ticks.label_prec = (2, 2)
s.maj_ticks.label_angle = math.pi / 4.0
s.maj_ticks.label_range = (10.0, 90.0)

mt = gauge.Ticks()
s.min_ticks.append(mt)
mt.count = 9
mt.length = 0.05
mt.range = (10.0, 100.0)
mt.pen.thickness = 0.003

mt = gauge.Ticks()
s.min_ticks.append(mt)
mt.count = 1
mt.length = 0.075
mt.range = (10.0, 100.0)
mt.pen.thickness = 0.005

s = gauge.scale.Object()
o.add_scale(s)
s.radius = 0.7
s.font.set_size(0.08)
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.range = (1.0, 10.0)
s.label.text = "D"
s.label.position = (0.78, -0.1)
s.label.rotation = math.pi / 2.0
s.span = math.pi
s.label_radius = 0.87
s.maj_shift = (0.0, 0.0)
s.pen.thickness = 0.003
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.08)
s.maj_ticks.length = -0.1
s.maj_ticks.label_prec = (0, 1)
s.maj_ticks.label_angle = math.pi / 4.0
s.maj_ticks.label_range = (1.0, 9.0)

s = gauge.scale.Object()
o.add_scale(s)
s.radius = 0.7
s.font.set_size(0.05)
s.set_type(gauge.scale.Type.LOGARITHMIC)
s.range = (10.0, 100.0)
s.label.text = ""  # D2
s.label.rotation = math.pi
s.span = math.pi
s.rotation = math.pi
s.label_radius = 0.87
s.maj_shift = (0.0, 0.0)
s.pen.thickness = 0.006
s.maj_ticks.count = 9
s.maj_ticks.label_font.set_size(0.08)
s.maj_ticks.length = -0.1
s.maj_ticks.label_prec = (2, 2)
s.maj_ticks.label_angle = math.pi / 4.0
s.maj_ticks.label_range = (10.0, 90.0)

mt = gauge.Ticks()
s.min_ticks.append(mt)
mt.count = 9
mt.length = -0.05
mt.range = (10.0, 100.0)
mt.pen.thickness = 0.003

mt = gauge.Ticks()
s.min_ticks.append(mt)
mt.count = 1
mt.length = -0.075
mt.range = (10.0, 100.0)
mt.pen.thickness = 0.005

e.export(o, "/tmp/kolya_rule.svg")
e.export(o, "/tmp/kolya_rule.png")
