# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Module of application class
"""

from PyQt5.QtWidgets import QApplication


class Object(QApplication):
    def __init__(self, argv: list[str]) -> None:
        super().__init__(argv)
