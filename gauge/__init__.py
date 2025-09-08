# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Package of the gauge entity and exporter
"""

import enum
import logging


class FixedColor(enum.Enum):
    WHITE = 0
    BLACK = 1
    RED = 2
    GREEN = 3
    BLUE = 4
    CYAN = 5
    MAGENTA = 6
    YELLOW = 7


class FontFace(enum.Enum):
    NONE = 0
    SANS = 1
    SERIF = 2
    MONO = 3


class Font:
    def __init__(self) -> None:
        self.face: FontFace = FontFace.SANS
        self.size: float = 0.1

    def from_dict(self, data) -> None:
        # Face property
        face_o = data.get("face")
        if face_o is None:
            logging.warning("No 'face' field in 'font' object")
        else:
            if not isinstance(face_o, str):
                raise Exception(
                    "The 'face' field in 'font' object is not  a string "
                    "value"
                )
            face = FontFace.NONE
            if face_o == "sans":
                face = FontFace.SANS
            elif face_o == "serif":
                face = FontFace.SERIF
            elif face_o == "mono":
                face = FontFace.MONO
            else:
                raise Exception(f"Value '{face_o}' is unknown font face")
            self.face = face

        # Size property
        size_o = data.get("size")
        if size_o is None:
            logging.warning("No 'size' field in 'font' object")
        else:
            if not isinstance(face_o, str):
                raise Exception(
                    "The 'size' field in 'font' object is not a floating point"
                    " real value"
                )
            self.size = size_o


class Color:
    def __init__(self) -> None:
        self.color = (0.0, 0.0, 0.0, 1.0)

    def from_fixed(self, fc: FixedColor) -> None:
        if fc == FixedColor.BLACK:
            self.color = (0.0, 0.0, 0.0, 1.0)
        elif fc == FixedColor.WHITE:
            self.color = (1.0, 1.0, 1.0, 1.0)
        elif fc == FixedColor.RED:
            self.color = (1.0, 0.0, 0.0, 1.0)
        elif fc == FixedColor.GREEN:
            self.color = (1.0, 1.0, 0.0, 1.0)
        elif fc == FixedColor.BLUE:
            self.color = (0.0, 0.0, 1.0, 1.0)
        elif fc == FixedColor.CYAN:
            self.color = (0.0, 0.0, 1.0, 1.0)
        elif fc == FixedColor.MAGENTA:
            self.color = (0.0, 0.0, 1.0, 1.0)
        elif fc == FixedColor.YELLOW:
            self.color = (0.0, 0.0, 1.0, 1.0)

    def from_dict(self, data) -> None:
        color_o = data.get("color")
        if color_o is None:
            raise Exception("No 'color' object")

        self.color = (color_o[0], color_o[1], color_o[2], color_o[3])

    @staticmethod
    def create_from_fixed(fc: FixedColor) -> "Color":
        c = Color()
        c.from_fixed(fc)
        return c


class Pen:
    def __init__(self) -> None:
        self.color = Color.create_from_fixed(FixedColor.BLACK)
        self.thickness = 0.01


class Label:
    def __init__(self) -> None:
        self.text: str = ""
        self.position: tuple[float, float] = (0.0, 0.0)
        self.rotation: float = 0.0
        self.font: Font = Font()

    def from_dict(self, data) -> None:
        text_o = data.get("text")
        if text_o is None:
            logging.warning("No 'text' field in 'label' object")
        else:
            if not isinstance(text_o, str):
                raise Exception(
                    "The 'text' field in 'label' object is not a string value"
                )
            self.text = text_o

        # Font property
        font_o = data.get("font")
        if font_o is None:
            logging.warning("No 'font' field in 'label' object")
        else:
            font = Font()
            font.from_dict(font_o)
            self.font = font

        # Position property
        position_o = data.get("position")
        if position_o is None:
            logging.warning("No 'position' field in 'label' object")
        else:
            if (
                (not isinstance(position_o, list))
                or len(position_o) != 2
                or (not all(isinstance(x, float) for x in position_o))
            ):
                raise Exception(
                    "The 'position' field in 'label' object is not a "
                    "tuple of 2 floating point real values"
                )
            self.position = (position_o[0], position_o[1])


class Ticks:
    def __init__(self) -> None:
        self.count = 1
        self.length = 0.1
        self.shift = 0.0
        self.pen: Pen = Pen()
        self.range: tuple[float, float] = (0.0, 1.0)
        self.label_range: tuple[float, float] = (0.0, 1.0)
        self.label_angle: float = -1.0
        self.label_font: Font = Font()
        self.label_prec: tuple[int, int] = (2, 2)
        self.draw_labels: bool = False

    def from_dict(self, data) -> None:
        count_o = data.get("count")
        if count_o is None:
            logging.warning("No 'count' field in 'ticks' object")
        else:
            if not isinstance(count_o, int):
                raise Exception(
                    "The 'count' field in 'ticks' object is not integer value"
                )
            self.count = count_o

        # Length property
        length_o = data.get("length")
        if length_o is None:
            logging.warning("No 'length' field in 'ticks' object")
        else:
            if not isinstance(length_o, float):
                raise Exception(
                    "The 'count' field in 'ticks' object is not real "
                    "numeric value"
                )
            self.length = length_o

        # Label range property
        label_range_o = data.get("label_range")
        if label_range_o is None:
            logging.warning("No 'label_range' field in 'ticks' object")
        else:
            if (
                (not isinstance(label_range_o, list))
                or len(label_range_o) != 2
                or (not all(isinstance(x, float) for x in label_range_o))
            ):
                raise Exception(
                    "The 'label_range' field in 'ticks' object is not a "
                    "tuple of 2 real values"
                )
            self.label_range = (label_range_o[0], label_range_o[1])

        # Label precision property
        label_prec_o = data.get("label_prec")
        if label_prec_o is None:
            logging.warning("No 'label_prec' field in 'ticks' object")
        else:
            if (
                (not isinstance(label_prec_o, list))
                or len(label_range_o) != 2
                or (not all(isinstance(x, int) for x in label_prec_o))
            ):
                raise Exception(
                    "The 'label_prec' field in 'ticks' object is not a "
                    "tuple of 2 int values"
                )
            self.label_prec = (label_prec_o[0], label_prec_o[1])

        # Label font property
        label_font_o = data.get("label_font")
        if label_font_o is None:
            logging.warning("No 'label_font' field in 'ticks' object")
        else:
            label_font = Font()
            label_font.from_dict(label_font_o)
            self.label_font = label_font


def normalize(val: float, a: float, b: float) -> float:
    return (val - a) / (b - a)


def clamp(val: float, a: float, b: float):
    return max(a, min(b, val))
