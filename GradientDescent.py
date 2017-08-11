import math

def readFile():
	file = open('/Users/nhonitus/Desktop/input.txt', 'r')
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
	n = len(theta) - 1
	sum = 0.0
	for i in range(0, n):
		sum += theta[i] * feature[i]
	return sum

def costFunction(theta, features, target):
	n = len(theta) - 1
	sum = 0.0
	for i in range (0, n):
		diff = cal(theta, features[i]) - target[i]
		sum += diff * diff
	return sum


def gradientDescent(theta, features, target):
	alpha = 0.00002775
	eps = 0.000000001
	n = len(target) - 1
	m = len(theta) - 1
	while (True):
		newtheta = theta
		for i in range(0, n):
			diff = cal(newtheta, features[i]) - target[i]
			diff *= alpha
			for j in range(0, m):
				newtheta[j] -= diff * features[i][j] / n
		t = True
		for i in range(0, m):
			t = t & (math.fabs(theta[i] - newtheta[i]) < eps)
		if (t == True):
			return newtheta
		theta = newtheta
				 


