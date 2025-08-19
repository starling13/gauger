# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Module of the exporter object class
"""

import math

import cairo

import gauge.round_gauge
import gauge.scale


class Object:
    """
    @brioef Exporter object

    Exports the gauge object to SVG-file
    """

    def __init__(self) -> None:
        pass

    def _draw_scale(
        self, s: gauge.scale.Object, context: cairo.Context
    ) -> None:
        """
        @brief Draw scale on gauge based on the scale object
        @param s -- scale object
        @param context -- cairo context object
        """

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
        step = (s.range[1] - s.range[0]) / (s.maj_ticks.count)

        i: int = 0
        while i <= s.maj_ticks.count:
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
                    context.rotate(angle + s.rotation)
                else:
                    context.rotate(s.maj_ticks.label_angle)
                context.scale(1.0, -1.0)
                val_str = f"{pos:{s.maj_ticks.label_prec[0]}.{s.maj_ticks.label_prec[1]}g}"
                ext = context.text_extents(val_str)
                context.move_to(
                    s.maj_shift[0] - ext.width / 2.0,
                    ext.height / 2.0 - s.maj_shift[1],
                )
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
                            context.rotate(c_angle + s.rotation)
                        else:
                            context.rotate(mt.label_angle)
                        context.scale(1.0, -1.0)
                        val_str = (
                            f"{c_pos:{mt.label_prec[0]}.{mt.label_prec[1]}g}"
                        )
                        ext = context.text_extents(val_str)
                        context.move_to(
                            s.maj_shift[0] - ext.width / 2.0,
                            ext.height / 2.0 - s.maj_shift[1],
                        )
                        context.show_text(val_str)
                        context.restore()

                    context.restore()

            i += 1
            pos = s.range[0] + i * step

    def _draw_labels(
        self, s: gauge.scale.Object, context: cairo.Context
    ) -> None:
        """
        @brief Draw out-of-scale labels
        @param s -- scale object
        @param context -- cairo context object
        """
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
        """
        @brief Export gauge object into image file
        @param obj -- Gauge object
        @param file_path -- path to the SVG-file
        """
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
        context.set_font_size(obj.label.font.size)

        context.move_to(obj.label.position[0], obj.label.position[1])
        context.scale(1, -1)
        context.show_text(obj.label.text)
        context.scale(1, -1)

        for s in obj.scales:
            context.new_path()
            context.set_source_rgba(
                s.color[0], s.color[1], s.color[2], s.color[3]
            )

            context.save()
            context.translate(s.position[0], s.position[1])
            context.rotate(s.rotation)
            self._draw_labels(s, context)
            context.new_path()
            self._draw_scale(s, context)
            context.restore()
