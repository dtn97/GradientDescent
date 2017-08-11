import numpy as np
import matplotlib.pyplot as plt
import array
import math
import random
import _thread
from GradientDescent import gradientDescent, getTrainingDataSet, readFile

def f(x, theta):
	return theta[0] * x * x * x + theta[1] * x * x + theta[2] * x + theta[3]

arr = readFile()
for i in arr:
	plt.scatter(i[0], i[1])

features, target = getTrainingDataSet(arr)

theta = [1.0, 1.0, 1.0, 1.0]

newtheta = gradientDescent(theta, features, target)

for i in newtheta:
	print(i, '\n')

x = np.arange(-25.0, 25.0, 0.01)
y = f(x, theta)
z = f(x, [3.0, -4.0, 4.0, 2.0])
plt.plot(x, z, 'r')
plt.plot(x, y, 'b')
plt.xlabel('x')
plt.ylabel('y')


plt.show()