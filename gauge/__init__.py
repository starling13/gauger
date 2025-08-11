import enum
import math


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
        self.label_precision: tuple[int, int] = (1, 0)
        self.draw_labels: bool = False


def normalize(val: float, a: float, b: float) -> float:
    return (val - a) / (b - a)


def clamp(val: float, a: float, b: float):
    return max(a, min(b, val))
