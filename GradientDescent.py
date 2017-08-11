import math

def readFile():
	file = open('/Users/nhonitus/Documents/Computer Vision/GradientDescent/input.txt', 'r')
	a = []
	for line in file:
		a.append(float(line))
	n = len(a)
	res = []
	for i in range(0, n - 1, 2):
		res.append([a[i], a[i + 1]])
	return res

def getTrainingDataSet(arr):
	features = []
	target = []
	for i in arr:
		features.append([i[0] * i[0] * i[0], i[0] * i[0], i[0], 1])
		target.append(i[1])
	return features, target

def cal(theta, feature):
	n = len(theta)
	sum = 0.0
	for i in range(0, n):
		sum += theta[i] * feature[i]
	return sum

def JFunction(theta, features, target):
	n = len(target)
	sum = 0.0
	for i in range (0, n):
		diff = cal(theta, features[i]) - target[i]
		sum += diff * diff
	return (sum) / (2 * (n))

def gradientDescent(theta, features, target):
	alpha = 0.0000002
	eps = 0.01
	n = len(target)
	m = len(theta)
	file = open('/Users/nhonitus/Documents/Computer Vision/GradientDescent/error.txt', 'w')
	while (True):
		newtheta = []
		for i in theta:
			newtheta.append(i)
		for j in range(0, m):
			diff = 0
			for i in range (0, n):
				diff += (cal(newtheta, features[i]) - target[i]) * alpha * features[i][j]
			newtheta[j] -= diff / n
		file.write(repr(JFunction(newtheta, features, target)) + '\n')
		error = math.fabs(JFunction(theta, features, target) - JFunction(newtheta, features, target))
		if error < eps:
			file.close()
			return newtheta
		for i in range(0, m):
			theta[i] = newtheta[i]
				 


