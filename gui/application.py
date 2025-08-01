"""
Created on 1 авг. 2025 г.

@author: skvortsov
"""

from PyQt5.QtWidgets import QApplication


class Object(QApplication):
    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)
