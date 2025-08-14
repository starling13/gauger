# Copyright (c) 2025 Andrey V. Skvortsov

# This work is licensed under the terms of the MIT license.
# For a copy, see COPYING file

"""
@brief Main module of the gui application
"""

import sys

import gui.application
import gui.main_window


def __main(argv: list[str]) -> int:
    res: int
    app: gui.application.Object
    mw: gui.main_window.Object

    app = gui.application.Object(argv)
    mw = gui.main_window.Object()
    mw.showMaximized()
    res = app.exec()

    return res


if __name__ == "__main__":
    sys.exit(__main(sys.argv))
