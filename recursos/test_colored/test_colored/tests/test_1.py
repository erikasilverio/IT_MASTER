#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test foreground and background colors with int numbers. """

from colored import fore, back, style


def main():

    for num in range(0, 256):
        print(f"{fore(num)}{num:>3}{style(0)}", end='  ')

    for num in range(0, 256):
        print(f"{back(num)}{num:>3}{style(0)}", end='  ')

    for name in range(0, 256):
        print(f"{style(4, name)}{name:>3}{style(59)}", end='  ')


if __name__ == '__main__':
    main()
