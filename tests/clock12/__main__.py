import gauge.exporter
import gauge.round_gauge
import gauge.scale

import math

# Main object for gauge
o = gauge.round_gauge.Object()

# First and the only scale of the classic clock
s = gauge.scale.Object()
# Add scale object to gauge before any other actions
# because it changes some properties of the scale
o.add_scale(scale_object=s)
# Rotate 90 deg CCW to orient 12 hour tick up
s.rotation = -math.pi / 2.0
# Scale has a radius of 0.9 of image half
s.radius = 0.9
# Scale span is 360 deg - full circle
s.span = math.pi * 2.0
# Setting the range of the clock [1; 12] hours, real numbers used.
s.range = (0.0, 12.0)
# Major tick and digit label on every hour
s.maj_ticks.count = 12
# Major ticks length is ~ 0.1 of the gauge radius
s.maj_ticks.length = 0.1
# Major ticks span range from 1 to 12, excluding 0 which has 12 mark as scale spans whole 360 deg. circle.
s.maj_ticks.label_range = (1.0, 12.0)
# Set precision of the hour digit labels: minimum 1 symbol, not longer then 2
s.maj_ticks.label_prec = (1, 2)
# Relative size of the hour labels font
s.maj_ticks.label_font.size = 0.15
# Face of the hour labels font
s.maj_ticks.label_font.face = gauge.FontFace.SANS

# Common label of the scale
s.label.text = "Toy clock"
# Common label position
s.label.position = (-0.25, -0.5)
# Font face for common label
s.label.font.face = gauge.FontFace.SERIF

# Minor ticks object
mt = gauge.Ticks()
# First of all add it to the scale
s.add_minor_ticks(ticks=mt)
# 4 ticks between hours on every minute
mt.count = 4
# Minor ticks are shorter then major
mt.length = 0.05

# SVG-exporter object
e = gauge.exporter.Object()
# Export the shining new gauge to file
e.export(obj=o, file_path="test.svg")
