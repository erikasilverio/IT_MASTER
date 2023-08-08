#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Test the nearest matching hex color lookup """

import time
from random import randint
from colored.hexadecimal import Hex
from colored import fore, back, style
from colored.library import Library


def compare_with_expected(in_hex, expected):
    """ Contribution by Fredrik Klasson. """
    hexad = Hex()
    nearest = hexad.find(in_hex)
    # Look up the matched hex value (e.g. xterm colors 10 and 46 are
    # the same hex value)
    match = Library.HEX_COLORS[nearest] == Library.HEX_COLORS[expected]

    e_str = '%s%s##%s' % (fore(expected), back(expected), style('reset'))
    n_str = '%s%s##%s' % (fore(nearest), back(nearest), style('reset'))
    print("%s: %s => %s = %s" % ('pass' if match else 'FAIL', in_hex, n_str, e_str))

    return match


def main():
    """ Contribution by Fredrik Klasson. """
    print('            Nearest   Expected')
    test_set = {
        '1': ('#7f0000', '#800000', '#810000'),
        '2': ('#007f00', '#008000', '#008100'),
        '4': ('#00007f', '#000080', '#000081'),
        '10': ('#00fe00', '#00ff00', '#01ff00'),
    }

    all_ok = True
    for expected, hexes in test_set.items():
        for hex_code in hexes:
            okay = compare_with_expected(hex_code, expected)
            all_ok = all_ok and okay

    try:
        T_sta = time.perf_counter()
        print('-' * 78)
        for y in range(0, 0xF):
            r_row = ''
            g_row = ''
            b_row = ''
            i_row = ''
            for x in range(0, 0xF):
                c = x + y * 0xF
                hex_code = '#%02x0000' % (c,)
                r_row += '%s%s#' % (fore(hex_code), back(hex_code))
                hex_code = '#00%02x00' % (c,)
                g_row += '%s%s#' % (fore(hex_code), back(hex_code))
                hex_code = '#0000%02x' % (c,)
                b_row += '%s%s#' % (fore(hex_code), back(hex_code))
                hex_code = '#' + ('%02x' % (c,)) * 3
                i_row += '%s%s#' % (fore(hex_code), back(hex_code))
                print('%s%s %s%s %s%s %s%s' % (
                    r_row, style('reset'), g_row, style('reset'), b_row, style('reset'), i_row, style('reset')))
        dT = time.perf_counter() - T_sta
        print('Lookup time: %0.4f s => %0.4f s/lookup' % (dT, dT / (2 * 4 * 0xFF)))
        print('-' * 78)
    except Exception as e:
        print('Whopsie, something %s-ish went wrong: %s' % (e.__class__.__name__, e))
        import traceback
        traceback.print_exc()
        all_ok = False

    # This is just for fun, almost... let's call it a
    # "non-deterministic check that it doesn't throw any exceptions"
    try:
        T_sta = time.perf_counter()
        for y in range(0, 20):
            for x in range(0, 30):
                rnd = randint(0, 0xffffff)
                hex_code = '#%06x' % (rnd,)
                hexinv = '#%06x' % (0xffffff - rnd,)
                print('%s%s::' % (fore(hexinv), back(hex_code)), end='')
            print(style('reset'))
        dT = time.perf_counter() - T_sta
        print('Lookup time: %0.4f s => %0.4f s/lookup' % (dT, dT / (2 * 30 * 20)))
    except Exception as e:
        print('Whopsie, something %s-ish went wrong: %s' % (e.__class__.__name__, e))
        all_ok = False

    return all_ok


if __name__ == "__main__":
    ok = main()
    exit(0 if ok else 1)
