"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

import math

import cairo

import gauge.round_gauge


class Object:
    def __init__(self) -> None:
        pass

    def _draw_linear_scale(
        self,
        s: gauge.scale.Object,
        context,
        maj_span: float,
        maj_span_rot: float,
        maj_step: float,
        maj_step_rot: float,
    ):
        context.set_line_width(s.pen.thickness)
        arc_start = math.pi * 2.0 - s.span
        arc_end = math.pi * 2.0
        context.arc(
            0.0,
            0.0,
            s.radius,
            arc_start,
            arc_end,
        )
        context.stroke()

        pos = 0.0
        while pos <= maj_span:
            context.save()

            context.rotate(-maj_span_rot * pos)
            context.move_to(s.radius + s.maj_ticks.shift, 0.0)
            context.line_to(
                s.radius + s.maj_ticks.shift - s.maj_ticks.length, 0.0
            )
            context.stroke()

            if maj_span - pos >= maj_step:
                for i in range(0, s.min_ticks.count):
                    context.rotate(-maj_step_rot / (s.min_ticks.count + 1))
                    context.move_to(s.radius + s.min_ticks.shift, 0.0)
                    context.line_to(
                        s.radius + s.min_ticks.shift - s.min_ticks.length,
                        0.0,
                    )
                    context.stroke()

            context.restore()

            pos += maj_step

    def _draw_logarithmic_scale(self, s, context) -> None:

        context.set_font_size(s.font.size)
        context.set_line_width(s.pen.thickness)
        arc_start = math.pi * 2.0 - s.span
        arc_end = math.pi * 2.0
        context.arc(
            0.0,
            0.0,
            s.radius,
            arc_start,
            arc_end,
        )
        context.stroke()

        pos = s.range[0]
        step = (s.range[1] - s.range[0]) / (s.maj_ticks.count + 1)

        i: int = 0
        while i <= s.maj_ticks.count + 1:
            # Current position angle
            angle = s.get_angle(pos)

            context.save()

            context.rotate(-angle)
            context.set_line_width(s.pen.thickness)
            context.move_to(s.radius + s.maj_ticks.shift, 0.0)
            context.line_to(
                s.radius + s.maj_ticks.shift - s.maj_ticks.length, 0.0
            )
            context.stroke()

            if (
                s.maj_ticks.label_range[0] <= pos
                and s.maj_ticks.label_range[1] >= pos
            ):
                context.save()
                context.translate(s.label_radius, 0.0)
                if s.maj_ticks.label_angle < 0.0:
                    context.rotate(angle - s.rotation)
                else:
                    context.rotate(s.maj_ticks.label_angle)
                context.scale(1.0, -1.0)
                context.move_to(s.maj_shift[0], -s.maj_shift[1])
                val_str = f"{pos:{s.maj_prec[0]}.{s.maj_prec[1]}g}"
                context.show_text(val_str)
                context.restore()

            context.restore()

            for mt in s.min_ticks:
                c_step = step / (mt.count + 1)
                c_pos: float = pos
                for j in range(1, mt.count + 1):
                    c_pos = pos + j * c_step
                    if mt.range[0] > c_pos or mt.range[1] <= c_pos:
                        continue
                    c_angle = s.get_angle(c_pos)
                    context.save()
                    context.rotate(-c_angle)
                    context.set_line_width(mt.pen.thickness)
                    context.move_to(s.radius + mt.shift, 0.0)
                    context.line_to(s.radius + mt.shift - mt.length, 0.0)
                    context.stroke()

                    if mt.draw_labels and (
                        mt.label_range[0] <= pos and mt.label_range[1] >= pos
                    ):
                        context.save()
                        context.set_font_size(mt.label_font.size)
                        context.translate(s.label_radius, 0.0)
                        if mt.label_angle < 0.0:
                            context.rotate(angle)
                        else:
                            context.rotate(mt.label_angle)
                        context.scale(1.0, -1.0)
                        context.move_to(s.maj_shift[0], -s.maj_shift[1])
                        val_str = f"{c_pos:{mt.label_precision[0]}.{mt.label_precision[1]}g}"
                        context.show_text(val_str)
                        context.restore()

                    context.restore()

            i += 1
            pos = s.range[0] + i * step

    def _draw_labels(self, s: gauge.scale.Object, context):
        gar = ""
        if s.font.face == gauge.FontFace.MONO:
            gar = "Monospace"
        elif s.font.face == gauge.FontFace.SANS:
            gar = "Arial"
        elif s.font.face == gauge.FontFace.SERIF:
            gar = "Serif"

        context.select_font_face(
            gar, cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD
        )
        context.set_font_size(s.font.size)

        context.save()
        context.rotate(-s.rotation)
        context.move_to(s.label.position[0], s.label.position[1])
        context.rotate(s.label.rotation)
        context.scale(1.0, -1.0)
        context.show_text(s.label.text)
        context.restore()

    def export(self, obj: gauge.round_gauge.Object, file_path: str) -> None:
        surface: cairo.SVGSurface = cairo.SVGSurface(
            file_path, obj.size[0], obj.size[1]
        )
        surface.set_document_unit(cairo.SVG_UNIT_PX)
        context: cairo.Context = cairo.Context(surface)

        # Make gauge area coordinates [-1; 1]
        context.scale(obj.size[0] / 2.0, -obj.size[1] / 2.0)
        context.translate(1, -1)

        # Gauge border
        context.set_line_width(obj.pen.thickness)
        context.arc(0, 0, obj.radius, 0, 2 * math.pi)
        context.stroke()

        # Label
        context.select_font_face(
            "Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD
        )
        context.set_font_size(0.08)

        context.move_to(obj.label.position[0], obj.label.position[1])
        context.scale(1, -1)
        context.show_text(obj.label.text)
        context.scale(1, -1)

        for s in obj.scales:
            context.new_path()
            context.set_source_rgba(
                s.color[0], s.color[1], s.color[2], s.color[3]
            )

            # Range of the major scale
            maj_span = s.range[1] - s.range[0]
            maj_span_rot = s.span / maj_span
            maj_step = maj_span / s.maj_ticks.count
            maj_step_rot = s.span / s.maj_ticks.count

            context.save()
            context.translate(s.position[0], s.position[1])
            context.rotate(s.rotation)
            self._draw_labels(s, context)
            context.new_path()
            self._draw_logarithmic_scale(s, context)
            context.restore()
