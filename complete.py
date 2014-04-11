#!/usr/bin/env python2.4
# -*- coding: utf-8 -*-

def get_divisor(number):
    """ 引数 number の約数をリストにして返す。
    >>> import complete
    >>> complete.get_divisor(6)
    [1, 2, 3]
    >>> complete.get_divisor(7)
    [1]
    >>> complete.get_divisor(100)
    [1, 2, 4, 5, 10, 20, 25, 50]
    """
    l = [cnt for cnt in range(1, number) if (number % cnt) == 0]
    return l

def is_complete(number):
    """ 数値が完全数かどうかを調べ、結果を bool 値で返す。"""
    multi = 0
    for num in get_divisor(number):
        multi += num
    if multi == number:
        return True;
    return False;

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    for cnt in xrange(1, 1001):
        if is_complete(cnt):
            print cnt,
