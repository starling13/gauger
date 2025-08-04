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

    def export(self, gauge: gauge.round_gauge.Object, file_path: str) -> None:
        surface: cairo.SVGSurface = cairo.SVGSurface(file_path, 800, 800)

        context: cairo.Context = cairo.Context(surface)

        context.scale(400, -400)
        context.translate(1, -1)

        # Border
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

            context.save()
            # Range of the major scale
            maj_span = s.range[1] - s.range[0]
            maj_span_rot = s.span / maj_span
            maj_step = maj_span / (s.maj_ticks)
            maj_step_rot = s.span / s.maj_ticks

            context.rotate(s.rotation)
            context.set_line_width(s.line)
            arc_start = math.pi * 2.0 - s.span
            arc_end = math.pi * 2.0
            context.arc(
                s.position[0],
                s.position[1],
                s.radius,
                arc_start,
                arc_end,
            )
            context.stroke()

            pos = 0.0
            while pos <= maj_span:
                context.save()

                context.rotate(-maj_span_rot * pos)
                context.move_to(s.radius, 0.0)
                context.line_to(s.radius - s.tick_len, 0.0)
                context.stroke()

                if maj_span - pos >= maj_step:
                    for i in range(0, s.min_ticks):
                        context.rotate(-maj_step_rot / (s.min_ticks + 1))
                        context.move_to(s.radius, 0.0)
                        context.line_to(s.radius - s.tick_len / 2.0, 0.0)
                        context.stroke()

                context.restore()

                pos += maj_step

            context.restore()

            context.save()
            pos = 0.0
            context.move_to(s.label.position[0], s.label.position[1])
            context.scale(1.0, -1.0)
            context.show_text(s.label.text)
            i = 0
            while pos <= maj_span:
                i += 1
                if i <= s.maj_ticks_start:
                    pos += maj_step
                    continue
                val = s.range[0] + pos
                val_str = f"{val:{s.maj_prec[0]}.{s.maj_prec[1]}f}"
                angle = -maj_span_rot * pos + s.rotation
                x = math.cos(angle) * s.label_radius + s.maj_shift[0]
                y = -math.sin(angle) * s.label_radius + s.maj_shift[1]
                context.move_to(x, y)
                context.show_text(val_str)
                pos += maj_step
            context.restore()
