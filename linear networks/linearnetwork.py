import random,pygame

############################linear network simple line division test######################################

#main perceptron class
class perceptron(object):
	def __init__(self,num_of_inputs):
		#initliaize
		self.weights = []
		for i in range(0,num_of_inputs):
			self.weights.append(random.randint(-10,10)/10.0)
		self.LEARNING_CONSTANT = 0.01

	def feedforward(self,inputs):
		#evaluate the inputs with the perceptron 
		sum = 0
		for j in range(0,len(inputs)):
			sum += inputs[j] * self.weights[j]
		sum += self.weights[2]
		return self.activate(sum)

	def activate(self,value):
		#the activation function
		if value > 0:
			return 1
		else:
			return -1

	def train(self,inputs,desired):
		#the training function
		guess = self.feedforward(inputs)
		difference = desired - guess
		for k in range(0,2):
			self.weights[k] += self.LEARNING_CONSTANT * difference * inputs[k]
		self.weights[2] += self.LEARNING_CONSTANT * difference


