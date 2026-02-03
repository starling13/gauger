# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Package of the gauge entity and exporter
"""

import enum
import logging
import math


class FixedColor(enum.Enum):
    """
    @brief Fixed colors enumeration

    Includes 16 colors from CGA palette
    """

    BLACK = 0
    BLUE = 1
    GREEN = 2
    CYAN = 3
    RED = 4
    MAGENTA = 5
    BROWN = 6
    LIGHT_GRAY = 7
    DARK_GRAY = 8
    LIGHT_BLUE = 9
    LIGHT_GREEN = 10
    LIGHT_CYAN = 11
    LIGHT_RED = 12
    LIGHT_MAGENTA = 13
    YELLOW = 14
    WHITE = 15


# AA hex integer as part of 255
__hex_AA = 170.0 / 255.0
# 55 hex integer as part of 255
__hex_55 = 55.0 / 255.0

_fixed_colors: list[tuple[float, float, float, float]] = [
    # BLACK 0
    (0.0, 0.0, 0.0, 1.0),
    # BLUE 1
    (0.0, 0.0, __hex_AA, 1.0),
    # GREEN 2
    (0.0, __hex_AA, 0.0, 1.0),
    # CYAN 3
    (0.0, __hex_AA, __hex_AA, 1.0),
    # RED 4
    (__hex_AA, 0.0, 0.0, 1.0),
    # MAGENTA 5
    (__hex_AA, 0.0, __hex_AA, 1.0),
    # BROWN 6
    (__hex_AA, __hex_55, 0.0, 1.0),
    # LIGHT_GRAY 7
    (__hex_AA, __hex_AA, __hex_AA, 1.0),
    # DARK_GRAY 8
    (__hex_55, __hex_55, __hex_55, 1.0),
    # LIGHT_BLUE 9
    (__hex_55, __hex_55, 1.0, 1.0),
    # LIGHT_GREEN 10
    (__hex_55, 1.0, __hex_55, 1.0),
    # LIGHT_CYAN 11
    (__hex_55, 1.0, 1.0, 1.0),
    # LIGHT_RED 12
    (1.0, __hex_55, __hex_55, 1.0),
    # LIGHT_MAGENTA 13
    (1.0, __hex_55, 1.0, 1.0),
    # YELLOW 14
    (1.0, 1.0, __hex_55, 1.0),
    # WHITE 15
    (1.0, 1.0, 1.0, 1.0),
]


class FontFace(enum.Enum):
    """
    @brief Font face enumeration
    """

    NONE = 0
    SANS = 1
    SERIF = 2
    MONO = 3


class Font:
    """
    @brief Class of the font object
    """

    def __init__(self) -> None:
        self.__face: FontFace = FontFace.SANS
        self.__size: float = 0.1

    @property
    def face(self) -> FontFace:
        """
        Font visual face
        """
        return self.__face

    def set_face(self, new_val: FontFace) -> None:
        self.__face = new_val

    @property
    def size(self) -> float:
        return self.__size

    def set_size(self, new_val: float) -> None:
        self.__size = new_val

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
            self.__face = face

        # Size property
        size_o = data.get("size")
        if size_o is None:
            logging.warning("No 'size' field in 'font' object")
        else:
            if not isinstance(size_o, float):
                raise Exception(
                    "The 'size' field in 'font' object is not a floating point"
                    " real value"
                )
            self.__size = size_o


class Color:
    def __init__(self) -> None:
        self.color = (0.0, 0.0, 0.0, 1.0)

    def from_fixed(self, fc: FixedColor) -> None:
        self.color = _fixed_colors[fc.value]

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
    """
    @brief Pen object
    """

    def __init__(self) -> None:
        self.color = Color.create_from_fixed(FixedColor.BLACK)
        self.thickness = 0.01


class Label:
    """
    @brief Label for the gauge or scale object
    """

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
    """
    @brief Regular ticks for the scale
    """

    def __init__(self) -> None:
        self.count = 1
        self.length = 0.1
        self.shift = 0.0
        self.pen: Pen = Pen()
        self.range: tuple[float, float] = (0.0, 1.0)
        self.label_range: tuple[float, float] = (0.0, 1.0)
        self.label_angle: float = math.nan
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
                or len(label_prec_o) != 2
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
