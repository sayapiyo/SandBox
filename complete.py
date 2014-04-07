#!/usr/bin/env python2.4
# -*- coding: utf-8 -*-

def get_divisor(number):
	""" 約数をリストにして返す
		>>> import complete
		>>> complete.get_divisor(6)
		[1, 2, 3]
		>>> complete.get_divisor(7)
		[1]
		>>> complete.get_divisor(100)
		[1, 2, 4, 5, 10, 20, 25, 50]
	"""
	l = []
	for cnt	in range(1,number):
		# number-1 までの約数を取り出す
		if number % (cnt) == 0:
			l.append(cnt)
	return l

def is_complete(number):
	""" 数値が完全数かどうかを調べ、結果をbool値で返す
	"""
	multi = 0
	for num in get_divisor(number):
		multi += num
	if multi == number:	return True;
	else:			return False;

if __name__ == "__main__":
	import doctest
	doctest.testmod()
	for cnt in xrange(1,1001):
		if is_complete(cnt):
			print cnt,
