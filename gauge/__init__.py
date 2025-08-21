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
    SANS = 0
    SERIF = 1
    MONO = 2


class Font:
    def __init__(self) -> None:
        self.face: FontFace = FontFace.SANS
        self.size: float = 0.1


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
        self.label_prec: tuple[float, float] = (2, 2)
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


def normalize(val: float, a: float, b: float) -> float:
    return (val - a) / (b - a)


def clamp(val: float, a: float, b: float):
    return max(a, min(b, val))
