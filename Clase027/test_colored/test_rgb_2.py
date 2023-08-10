#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Tests foreground and background RGB colors with numbers percentages. """

import time
from colored import Fore, Back, Style
from colored.controls import Controls
from colored.utilities import Utilities


def foreground():
    n = 0
    control = Controls()
    utils = Utilities()
    print("Press '[CTRL] + C' to interrupt:\n")
    print(f'{"":>7}FOREGROUND {"":>9}COLOR {"":>8}BACKGROUND')
    try:
        while True:
            n += 1
            per: str = f'{n}%'
            code: str = utils.convert_percentages(per)
            print(f'\r[{Fore.rgb(code, 0, 0)} Red {Style.reset}]'
                  f'[{Fore.rgb(0, code, 0)} Green {Style.reset}]'
                  f'[{Fore.rgb(0, 0, code)} Blue {Style.reset}] [ {per:>4} ] '
                  f'[{Back.rgb(code, 0, 0)} Red {Style.reset}]'
                  f'[{Back.rgb(0, code, 0)} Green {Style.reset}]'
                  f'[{Back.rgb(0, 0, code)} Blue {Style.reset}]',
                  end='')
            if n == 100:
                n = 0
                print(control.nav('erase_line', 1), end='')
                time.sleep(1)
            time.sleep(0.01)
    except KeyboardInterrupt:
        pass


def main():

    foreground()


if __name__ == '__main__':
    main()
