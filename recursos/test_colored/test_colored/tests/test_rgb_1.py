#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tests foreground and background RGB colors with numbers. """

import os
import time
from colored import Fore, Back, Style
from colored.controls import Controls
from colored.utilities import Utilities
from colored.library import Library


def foreground():
    code = 0
    control = Controls()
    utils = Utilities()
    utils.set_colorterm(colorterm='truecolor')
    max_range: int = Library.COLORTERM[os.environ['COLORTERM']]
    print("Press '[CTRL] + C' to interrupt:\n")
    print(f'{"":>7}FOREGROUND {"":>8}COLOR {"":>8}BACKGROUND')
    try:
        while True:
            code += 1
            print(f'\r[{Fore.rgb(code, 0, 0)} Red {Style.reset}]'
                  f'[{Fore.rgb(0, code, 0)} Green {Style.reset}]'
                  f'[{Fore.rgb(0, 0, code)} Blue {Style.reset}] [ {code:>3} ] '
                  f'[{Back.rgb(code, 0, 0)} Red {Style.reset}]'
                  f'[{Back.rgb(0, code, 0)} Green {Style.reset}]'
                  f'[{Back.rgb(0, 0, code)} Blue {Style.reset}]',
                  end='')
            if code == max_range:
                code = 0
                print(control.nav('erase_line', 1), end='')
                time.sleep(1)
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass


def main():

    foreground()


if __name__ == '__main__':
    main()
