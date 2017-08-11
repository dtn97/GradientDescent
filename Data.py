import numpy as np
import array
import math
import random

arr = []
a = 3
b = -5
c = 4
d = 2
i = -20.0
while (i <= 20.0):
	x = i
	y = a * x * x * x + b * x * x + c * x + d
	#arr.append([x + random.uniform(-1.0, 1.0), y])
	arr.append([x, y + random.uniform(0.0, 1.0)])
	#arr.append([x + random.uniform(-1.0, 1.0), y + random.uniform(-1.0, 1.0)])
	#arr.append([x, y])
	#arr.append([x - random.uniform(-1.0, 1.0), y + random.uniform(-1.0, 1.0)])
	i += 0.2

file = open('/Users/nhonitus/Documents/Computer Vision/GradientDescent/input1.txt', 'w')

for i in arr:
	file.write(repr(i[0]) + '\n')
	file.write(repr(i[1]) +  '\n')
	print(i[0], ' ', i[1], '\n')

file.close()