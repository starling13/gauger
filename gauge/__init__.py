import enum
import math


class FontFace(enum.Enum):
    SANS = 0
    SERIF = 1
    MONO = 2


class Font:
    def __init__(self) -> None:
        self.face: FontFace = FontFace.SANS
        self.size: float = 0.1


class Label:
    def __init__(self) -> None:
        self.text: str = ""
        self.position: tuple[float, float] = (0.0, 0.0)
        self.font: Font = Font()


class Ticks:
    def __init__(self) -> None:
        self.count = 1
        self.length = 0.1
        self.shift = 0.0
