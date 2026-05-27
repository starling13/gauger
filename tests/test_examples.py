import math
import os
import pathlib

import gauge
import gauge.exporter
import gauge.round_gauge


def test_basic_gauge(tmp_path):
    gauge1 = gauge.round_gauge.Object()

    scale1 = gauge.scale.Object()
    gauge1.add_scale(scale_object=scale1)
    scale1.range = (0.0, 10.0)
    scale1.maj_ticks.count = 10

    mt1 = gauge.Ticks()
    scale1.add_minor_ticks(ticks=mt1)
    mt1.count = 1

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "gauge1.png"
    exporter.export(gauge1, out_file)
    assert out_file.exists()


def test_clock_ruler(tmp_path):
    """
    @brief Pocket clock-like circular sliding ruler from USSR
    """
    ruler_ussr = gauge.round_gauge.Object()
    ruler_ussr.size = (1024, 1024)

    s: gauge.scale.Object = gauge.scale.Object()
    ruler_ussr.add_scale(s)
    s.set_type(gauge.scale.Type.LOGARITHMIC)
    s.range = (1.0, 10.0)
    s.span = math.pi
    s.radius = 0.85
    s.label_radius = 0.9
    s.maj_ticks.label_font.size = 0.075
    s.maj_ticks.count = 9
    s.maj_ticks.pen.thickness = 0.005
    s.maj_ticks.label_angle = -math.pi / 2.0
    s.maj_ticks.shift = 0.12
    s.maj_ticks.length = 0.12

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.1

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.075
    mt.length = 0.075
    mt.count = 9
    mt.range = (1.0, 2.0)

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.03
    mt.length = 0.03
    mt.count = 19
    mt.range = (1.0, 2.0)

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.03
    mt.length = 0.03
    mt.count = 9
    mt.range = (2.0, 6.0)

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.03
    mt.length = 0.03
    mt.count = 3
    mt.range = (6.0, 10.0)

    s: gauge.scale.Object = gauge.scale.Object()
    ruler_ussr.add_scale(s)
    s.set_type(gauge.scale.Type.LOGARITHMIC)
    s.range = (10.0, 100.0)
    s.span = math.pi
    s.radius = 0.85
    s.label_radius = 0.9
    s.maj_ticks.label_range = (20.0, 90.0)
    s.rotation = math.pi
    s.maj_ticks.count = 9
    s.maj_ticks.label_font.size = 0.075
    s.maj_ticks.label_prec = (3, 3)
    s.maj_ticks.label_angle = -math.pi / 2.0
    s.maj_ticks.shift = 0.12
    s.maj_ticks.length = 0.12
    s.maj_ticks.pen.thickness = 0.005
    s.maj_ticks.angle_shift = -0.03

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.1

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.075
    mt.length = 0.075
    mt.count = 9
    mt.range = (10.0, 20.0)

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.03
    mt.length = 0.03
    mt.count = 19
    mt.range = (10.0, 20.0)

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.03
    mt.length = 0.03
    mt.count = 9
    mt.range = (20.0, 60.0)

    mt = gauge.Ticks()
    s.add_minor_ticks(mt)
    mt.pen.thickness = 0.005
    mt.shift = 0.03
    mt.length = 0.03
    mt.count = 3
    mt.range = (60.0, 100.0)

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "ruler_ussr.png"
    exporter.export(ruler_ussr, out_file)
    assert out_file.exists()


def test_thermometer(tmp_path):
    """
    @brief Thermometer for steam boiler / BWR

    Scaled in celsium and fahrenheit degrees
    """
    thermometer = gauge.round_gauge.Object()
    thermometer.size = (1024, 1024)
    thermometer.set_radius(0.99)

    s = gauge.scale.Object()
    thermometer.add_scale(s)
    s.rotation = 0.0
    s.radius = 0.8
    s.pen.thickness = 0.005
    s.range = (10.0, 410.0)

    sec = gauge.scale.ScaleSector()
    sec.range = (10.0, 30.0)
    sec.radius_range = (0.3, 0.97)
    sec.color = gauge.Color.create_from_fixed(fc=gauge.FixedColor.LIGHT_CYAN)
    s.add_sector(sec)
    sec = gauge.scale.ScaleSector()
    sec.range = (100.0, 250.0)
    sec.radius_range = (0.3, 0.97)
    sec.color = gauge.Color.create_from_fixed(
        fc=gauge.FixedColor.LIGHT_MAGENTA
    )
    s.add_sector(sec)

    s.span = math.pi * 1.9
    s.label_radius = 0.91
    s.maj_ticks.label_font.face = gauge.FontFace.SERIF
    s.maj_ticks.pen.thickness = 0.006
    s.maj_ticks.length = -0.05
    s.maj_ticks.label_font.size = 0.05
    # s.maj_ticks.label_angle = 3.0 * math.pi / 2.0
    s.maj_ticks.label_prec = (0, 3)
    s.maj_ticks.count = 19
    s.maj_ticks.range = (20.0, 400.0)
    s.maj_ticks.label_range = (20.0, 510.0)

    mt1 = gauge.Ticks()
    s.add_minor_ticks(ticks=mt1)
    mt1.count = 9
    mt1.length = -0.02
    mt1.pen.thickness = 0.003

    mt2 = gauge.Ticks()
    s.add_minor_ticks(ticks=mt2)
    mt2.count = 1
    mt2.length = -0.04
    mt2.pen.thickness = 0.004

    s = gauge.scale.Object()
    thermometer.add_scale(s)
    s.rotation = 0.0
    s.radius = 0.79
    s.pen.thickness = 0.005

    s.range = (50.0, 770.0)
    s.span = math.pi * 1.9
    s.label_radius = 0.67
    s.maj_ticks.label_font.face = gauge.FontFace.SERIF
    s.maj_ticks.pen.thickness = 0.006
    s.maj_ticks.length = 0.05
    s.maj_ticks.label_font.size = 0.05
    # s.maj_ticks.label_angle = 3.0 * math.pi / 2.0
    s.maj_ticks.label_prec = (0, 3)
    s.maj_ticks.count = 23
    s.maj_ticks.range = (60.0, 750.0)
    s.maj_ticks.label_range = (60.0, 750.0)

    mt1 = gauge.Ticks()
    s.add_minor_ticks(ticks=mt1)
    mt1.count = 5
    mt1.length = 0.02
    mt1.pen.thickness = 0.003

    mt2 = gauge.Ticks()
    s.add_minor_ticks(ticks=mt2)
    mt2.count = 2
    mt2.length = 0.04
    mt2.pen.thickness = 0.004

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "BWR_thermo.svg"
    exporter.export(thermometer, out_file)
    assert out_file.exists()


def test_naval_astrolabe(tmp_path):
    sq_gauge = gauge.round_gauge.Object()
    sq_gauge.size = (1024, 1024)
    sq_gauge.set_radius(0.99)

    s = gauge.scale.Object()
    sq_gauge.add_scale(s)
    s.rotation = math.pi
    s.radius = 0.99

    s.range = (180.0, -180.0)
    s.span = math.pi * 2.0
    s.label_radius = 0.9
    s.maj_ticks.pen.thickness = 0.006
    s.maj_ticks.length = 0.06
    s.maj_ticks.label_font.size = 0.05
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

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "naval_astrolabe.svg"
    exporter.export(sq_gauge, out_file)
    assert out_file.exists()


def test_spiral_scale(tmp_path):
    sq_gauge = gauge.round_gauge.Object()

    scale1 = gauge.scale.Object()
    scale1.rotation = -0.3
    scale1.range = (1, 3000)
    scale1.maj_ticks.count = 20
    scale1.maj_ticks.label_font.size = 0.05
    scale1.label_radius = 0.8
    scale1.span = 20.0
    scale1.narrowing = 0.035
    scale1.maj_ticks.label_angle = math.pi / 2.0

    sq_gauge.add_scale(scale1)

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "sq_gauge.svg"
    exporter.export(sq_gauge, out_file)
    assert out_file.exists()


def test_manometer(tmp_path):
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

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "manometer.svg"
    exporter.export(o, out_file)
    assert out_file.exists()


def test_clock(tmp_path):
    o = gauge.round_gauge.Object()

    s = gauge.scale.Object()
    o.add_scale(s)

    s.rotation = -math.pi / 2.0
    s.radius = 0.9
    s.span = math.pi * 2.0
    s.range = (0.0, 12.0)
    s.maj_ticks.count = 12
    s.maj_ticks.length = 0.1
    s.maj_ticks.label_range = (1.0, 12.0)
    s.maj_ticks.label_prec = (1, 2)
    s.maj_ticks.label_font.size = 0.15
    s.maj_ticks.label_font.face = gauge.FontFace.SANS
    s.label.text = "Toy clock"
    s.label.position = (-0.25, -0.5)
    s.label.font.face = gauge.FontFace.SERIF
    mt = gauge.Ticks()
    s.add_minor_ticks(ticks=mt)
    mt.count = 4
    mt.length = 0.05
    # mt.range = (0.0, 12.0)

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "clock.svg"
    exporter.export(o, out_file)
    assert out_file.exists()


def test_simple_logarithmic_multiplyer(tmp_path):
    """
    @brief Simple circular logaritmic ruler

    Suitable for calculating multiplication table for integers from 1 to 9
    """
    o = gauge.round_gauge.Object()
    o.label.text = "Logarithmic multiplyer"
    o.label.position = (-0.45, -0.1)
    o.label.font.size = 0.065
    o.pen.color.from_fixed(gauge.FixedColor.BLACK)
    o.pen.thickness = 0.005
    o.size = (4096, 4096)

    s = gauge.scale.Object()
    o.add_scale(s)
    s.radius = 0.7
    s.font.size = 0.08
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
    s.maj_ticks.label_font.size = 0.07
    s.maj_ticks.length = 0.08
    s.maj_ticks.label_prec = (0, 1)
    s.maj_ticks.label_angle = math.pi / 4.0
    s.maj_ticks.label_range = (1.0, 9.0)

    s = gauge.scale.Object()
    o.add_scale(s)
    s.radius = 0.7
    s.font.size = 0.05
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
    s.maj_ticks.label_font.size = 0.07
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
    s.font.size = 0.08
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
    s.maj_ticks.label_font.size = 0.08
    s.maj_ticks.length = -0.1
    s.maj_ticks.label_prec = (0, 1)
    s.maj_ticks.label_angle = math.pi / 4.0
    s.maj_ticks.label_range = (1.0, 9.0)

    s = gauge.scale.Object()
    o.add_scale(s)
    s.radius = 0.7
    s.font.size = 0.05
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
    s.maj_ticks.label_font.size = 0.08
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

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "mult_rule.svg"
    exporter.export(o, out_file)
    assert out_file.exists()

    out_file = tmp_path / "mult_rule.png"
    exporter.export(o, out_file)
    assert out_file.exists()


def test_simple_clock(tmp_path):
    o = gauge.round_gauge.Object()

    s = gauge.scale.Object()
    o.add_scale(s)

    s.rotation = -math.pi / 2.0
    s.radius = 0.9
    s.span = math.pi * 2.0
    s.range = (0.0, 12.0)
    s.maj_ticks.count = 12
    s.maj_ticks.length = 0.1
    s.maj_ticks.label_range = (1.0, 12.0)
    s.maj_ticks.label_prec = (1, 2)
    s.maj_ticks.label_font.dize = 0.15
    s.maj_ticks.label_font.face = gauge.FontFace.SANS
    s.label.text = "Toy clock"
    s.label.position = (-0.25, -0.5)
    s.label.font.face = gauge.FontFace.SERIF
    mt = gauge.Ticks()
    s.add_minor_ticks(ticks=mt)
    mt.count = 4
    mt.length = 0.05
    # mt.range = (0.0, 12.0)

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "simple_clock.png"
    exporter.export(o, out_file)
    assert out_file.exists()


def test_complex_clock(tmp_path):
    # Create and initialize the main gauge object
    o = gauge.round_gauge.Object()

    # Create the primary 24-hour scale
    s = gauge.scale.Object()
    # Add scale object to gauge before any other actions
    # because it changes some properties of the scale
    o.add_scale(scale_object=s)
    # Orient the scale: rotate 90° counter-clockwise so 12 o'clock points upward
    s.rotation = -math.pi / 2.0

    # Configure scale geometry
    s.radius = 0.95  # Scale radius as fraction of half the image dimension
    s.span = math.pi * 2.0  # Full 360° circular scale

    # Define the value range: 0–24 hours (using floats here!)
    s.range = (0.0, 24.0)

    s.maj_ticks.count = 12  # 12 major divisions (0, 2, 4, ..., 22)
    s.maj_ticks.length = 0.1  # Tick length
    # Major ticks span range from 1 to 24, excluding 0 which has 24 mark as scale spans whole 360 deg. circle.
    s.maj_ticks.label_range = (1.0, 24.0)
    # Set precision of the hour digit labels: minimum 1 symbol, not longer then 2
    s.maj_ticks.label_prec = (1, 2)
    # Relative size of the hour labels font
    s.maj_ticks.label_font.size = 0.11
    # Face of the hour labels font
    s.maj_ticks.label_font.face = gauge.FontFace.SANS
    # Set radius of the virtual circle along which labels are placed
    s.label_radius = 0.75

    # Common label of the scale
    s.label.text = "Tank clock"
    # Common label position
    s.label.position = (-0.3, 0.4)
    # Font face for common label
    s.label.font.face = gauge.FontFace.MONO

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
    mt.label_font.size = 0.075
    # Minor ticks span range from 0 to 24, so to add mark on 1 hour
    mt.label_range = (0.0, 24.0)
    # Set precision of the hour digit labels: minimum 1 symbol, not longer then 2
    mt.label_prec = (1, 2)

    # Minor ticks for main scale minutes:
    mt = gauge.Ticks()
    s.add_minor_ticks(ticks=mt)
    # 4 ticks forms 5 intervals for minutes between hour ticks
    mt.count = 4
    # Shorter then odd hours ticks
    mt.length = 0.04

    # Additional scale for stopwatch/timer
    s = gauge.scale.Object()
    o.add_scale(s)
    s.rotation = -math.pi / 2.0
    # Auxilliary scale is shifted to the bottom
    s.position = (0, -0.3)
    # It's much smaller then main scale
    s.radius = 0.33
    s.span = math.pi * 2.0
    # Whole circle is 60 min/sec
    s.range = (0.0, 60.0)
    # A dozen of 5-min/sec ticks
    s.maj_ticks.count = 12
    s.maj_ticks.label_prec = (1, 2)
    s.maj_ticks.label_range = (0.0, 55.0)

    # Ticks for single minutes/seconds
    mt = gauge.Ticks()
    s.add_minor_ticks(ticks=mt)
    mt.count = 4
    mt.length = 0.02
    mt.range = (0.0, 60.0)
    s.maj_ticks.count = 12
    s.maj_ticks.length = 0.04
    s.maj_ticks.label_font.size = 0.06
    s.label_radius = 0.23

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "complex_clock.png"
    exporter.export(o, out_file)
    assert out_file.exists()


def test_manometer(tmp_path):
    o = gauge.round_gauge.Object()
    o.label.text = "Pressure"
    o.label.position = (-0.18, -0.2)

    s = gauge.scale.Object()
    s.rotation = math.pi / 2.0
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
    s.rotation = math.pi / 2.0 + start_angle
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

    exporter = gauge.exporter.Object()
    out_file = tmp_path / "manometer.png"
    exporter.export(o, out_file)
    assert out_file.exists()


if __name__ == "__main__":
    test_clock_ruler(tmp_path=pathlib.Path("/tmp"))
    test_thermometer(tmp_path=pathlib.Path("/tmp"))
    test_naval_astrolabe(tmp_path=pathlib.Path("/tmp"))
    test_spiral_scale(tmp_path=pathlib.Path("/tmp"))
    test_simple_clock(tmp_path=pathlib.Path("/tmp"))
    test_complex_clock(tmp_path=pathlib.Path("/tmp"))
    test_simple_logarithmic_multiplyer(tmp_path=pathlib.Path("/tmp"))
    test_manometer(tmp_path=pathlib.Path("/tmp"))
