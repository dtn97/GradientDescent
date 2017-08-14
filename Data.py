import numpy as np
import array
import math
import random

arr = []
a = 3
b = -5
c = 4
d = 2
i = -3.0
while (i <= 3.0):
	x = i
	y = a * x * x * x + b * x * x + c * x + d
	arr.append([x, y])
	i += 0.001

file = open('/Users/nhonitus/Documents/Computer Vision/GradientDescent/input2.txt', 'w')

for i in arr:
	file.write(repr(i[0]) + '\n')
	file.write(repr(i[1]) +  '\n')
	print(i[0], ' ', i[1], '\n')

file.close()