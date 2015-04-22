import math

def Sigmoid(x):
	return 1/(1+math.exp(-x))


class Sigmoid_Neuron(object):
	def __init__(self,weights):
		self.weights = weights

	def feedForward(self,inputs):
		sum = 0
		for i in range(0,len(inputs)):
			sum += self.weights[i] * inputs[i]
		sum += self.bias * self.weights[-1]
		return Sigmoid(sum)
