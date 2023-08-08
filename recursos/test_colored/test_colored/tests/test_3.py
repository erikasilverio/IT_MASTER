#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test foreground and background colors """

from colored.library import Library
from colored import fore, back, style


def main():

    for name in Library.HEX_COLORS.values():
        print(f"{fore(name)}{name:>3}", end='  ')

    for name in Library.HEX_COLORS.values():
        print(f"{back(name)}{name:>3}", end='  ')

    print(style('reset'))  # Reset all attributes


if __name__ == '__main__':
    main()
