#!/usr/bin/env python2.4
# -*- coding: utf-8 -*-

def get_divisors(number):
    """ 引数 number の約数をリストにして返す。
    >>> import complete
    >>> complete.get_divisors(6)
    [1, 2, 3]
    >>> complete.get_divisors(7)
    [1]
    >>> complete.get_divisors(100)
    [1, 2, 4, 5, 10, 20, 25, 50]
    """
    l = [cnt for cnt in range(1, number) if (number % cnt) == 0]
    return l

# TODO: 名称的には perfect number が正しい
#
def is_complete(number):
    """ 数値が完全数かどうかを調べ、結果を bool 値で返す。"""
    divisors = get_divisors(number)
    if sum(divisors) == number:
        return True;
    return False;

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    for cnt in xrange(1, 1001):
        if is_complete(cnt):
            print cnt,
