import random,pygame


class perceptron(object):
	def __init__(self):
		self.weights = []
		for i in range(0,3):
			self.weights.append(random.randint(-10,10)/10.0)
		self.LEARNING_CONSTANT = 0.01

	def feedforward(self,inputs):
		sum = 0
		for j in range(0,len(inputs)):
			sum += inputs[j] * self.weights[j]
		sum += self.weights[2]
		return self.activate(sum)

	def activate(self,value):
		if value > 0:
			return 1
		else:
			return -1

	def train(self,inputs,desired):
		guess = self.feedforward(inputs)
		difference = desired - guess
		for k in range(0,2):
			self.weights[k] += self.LEARNING_CONSTANT * difference * inputs[k]
		self.weights[2] += self.LEARNING_CONSTANT * difference


p = perceptron()

for m in range(0,100):
	x = random.randint(-200,200)
	y = random.randint(-200,200)
	if y > -0.2*x:
		ans = 1
	else:
		ans = -1
	p.train((x,y),ans)


window = pygame.display.set_mode((1000,1000))
window.fill((255,255,255))


for m in range(0,100000):
    x = random.randint(-500,500)
    y = random.randint(-500,500)

    dotg = pygame.Surface((10,10))
    dotg.fill((255,255,255))
    pygame.draw.circle(dotg,(255,0,0),(5,5),5,0)

    dotr = pygame.Surface((10,10))
    dotr.fill((255,255,255))
    pygame.draw.circle(dotr,(0,255,0),(5,5),5,0)
    
    if p.feedforward((x,y,1)) == 1:
        window.blit(dotg,(x+500,500-y))
    else:
        window.blit(dotr,(x+500,500-y))

pygame.display.flip()

j = 1
while j:
    for event in pygame.event.get():
        if event.type == 12:
            j = 0