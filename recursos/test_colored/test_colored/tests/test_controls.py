#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
from colored.controls import Controls


def main():

    moves: dict = {
        'down': 10,
        'up': 7,
        'right': 20,
        'left': 5,
        'previous': 10,
        'horizontal': 5,
        'erase_display': 2,
        'erase_line': 5,
        'scroll_up': 3,
        'scroll_down': 10
    }

    control = Controls()
    for move, row in moves.items():
        print(f'{move} {control.nav(move, row)}')
        time.sleep(1)

    print(f"position 4, 5 {control.nav('position', 4, 5)}")


if __name__ == '__main__':
    main()
