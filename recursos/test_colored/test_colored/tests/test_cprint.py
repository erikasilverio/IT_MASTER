#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test cprint(text: str,
           fore_256: int | str = '',
           back_256: int | str = '',
           fore_rgb: tuple = (255, 255, 255),
           back_rgb: tuple = (0, 0, 0),
           formatting: int | str = '',
           line_color: int | str = '',
           reset=True,
           **kwargs) function.
"""

import random
from colored.library import Library
from colored.cprint import cprint


def main():

    for color in Library.COLORS.values():
        back: int = random.randint(0, 255)
        a: int = random.randint(0, 255)
        b: int = random.randint(0, 255)
        c: int = random.randint(0, 255)
        style: str = random.choice(list(Library.STYLES.values()))
        cprint(' Hello World or World Hello? ', fore_256=color, back_256=back, formatting=style)
        cprint(' Hello World or World Hello? ', fore_rgb=(a, b, c), back_rgb=(c, b, a), formatting=style)


if __name__ == '__main__':
    main()
