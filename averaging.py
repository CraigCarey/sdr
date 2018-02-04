#!/usr/bin/env python

import math
import cmath
import matplotlib.pyplot as plt

tau = 2 * math.pi
base = math.e ** (1j * tau / 360)

def average(readings):
	total = 0
	ax = plt.axes()
	for r in readings:
		v = r[1] * base ** r[0]
		total += v
		ax.arrow(0, 0, v.real, v.imag, head_width=0.05, head_length=0.05, fc='r', ec='r')

	result = total / len(readings)
	ax.arrow(0, 0, result.real, result.imag, head_width=0.05, head_length=0.05, fc='b', ec='b')
	plt.xlim((-1.5, 1.5))
	plt.ylim((-1.5, 1.5))
	plt.xlabel('Real')
	plt.ylabel('Imaginary')
	plt.show()
	return cmath.log(result, base).real, abs(result)

res = average(((12, 1), (15, 1), (13, 1), (9, 10), (16, 1)))
print(res)

res = average(((358, 1), (1, 1), (359, 1), (355, 1), (2,1)))
print(res)

res = average(((210, 1), (290, 1), (10, 1), (90, 1), (170,1)))
print(res)

res = average(((170, 1), (171, 1), (180, 1), (181, 1), (190, 1)))
print(res)
