#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test foreground and background colors """

from colored import Fore, Back, Style
from colored.library import Library


def main():

    for color in Library.COLORS.keys():
        print(f"{getattr(Fore, color)} This is the color {color} {Style.RESET}")

    for color in Library.COLORS.keys():
        print(f"{getattr(Back, color)} This is the color {color:>20} {Style.RESET}")


if __name__ == '__main__':
    main()
