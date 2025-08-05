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
        context.translate(s.position[0], s.position[1])
        context.rotate(s.rotation)

        context.set_line_width(s.line)
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

    def _draw_logarithmic_scale(self, s, context):
        pass

    def _draw_labels(
        self,
        s: gauge.scale.Object,
        context,
        maj_span: float,
        maj_span_rot: float,
        maj_step: float,
    ):
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

        context.move_to(s.label.position[0], s.label.position[1])
        context.scale(1.0, -1.0)
        context.show_text(s.label.text)
        i = 0
        pos = 0.0
        while pos <= maj_span:
            i += 1
            if i <= s.maj_ticks_start:
                pos += maj_step
                continue
            val = s.range[0] + pos
            val_str = f"{val:{s.maj_prec[0]}.{s.maj_prec[1]}f}"
            angle = -maj_span_rot * pos + s.rotation
            x = (
                math.cos(angle) * s.label_radius
                + s.maj_shift[0]
                + s.position[0]
            )
            y = (
                -math.sin(angle) * s.label_radius
                - s.maj_shift[1]
                - s.position[1]
            )
            context.move_to(x, y)
            context.show_text(val_str)
            pos += maj_step

    def export(self, gauge: gauge.round_gauge.Object, file_path: str) -> None:
        surface: cairo.SVGSurface = cairo.SVGSurface(
            file_path, gauge.size[0], gauge.size[1]
        )
        context: cairo.Context = cairo.Context(surface)

        # Make gauge area coordinates [-1; 1]
        context.scale(gauge.size[0] / 2.0, -gauge.size[1] / 2.0)
        context.translate(1, -1)

        # Gauge border
        context.set_line_width(gauge.border_width)
        context.arc(0, 0, gauge.radius, 0, 2 * math.pi)
        context.stroke()

        # Label
        context.select_font_face(
            "Arial", cairo.FONT_SLANT_NORMAL, cairo.FONT_WEIGHT_BOLD
        )
        context.set_font_size(0.08)

        context.move_to(gauge.label.position[0], gauge.label.position[1])
        context.scale(1, -1)
        context.show_text(gauge.label.text)
        context.scale(1, -1)

        for s in gauge.scales:
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
            self._draw_linear_scale(
                s, context, maj_span, maj_span_rot, maj_step, maj_step_rot
            )
            context.restore()

            context.save()
            self._draw_labels(
                s,
                context,
                maj_span,
                maj_span_rot,
                maj_step,
            )
            context.restore()
