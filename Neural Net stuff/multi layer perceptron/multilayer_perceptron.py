import csv
from random import random
from random import seed
import math
# file to be imported
file = 'iris.csv'




# open file
with open(file, newline='') as csvfile:
    # init data to list of empty objs
    data = []

    # for each row in the file
    for row in csv.reader(csvfile, delimiter=','):
        # append whole row as an obj. 'row' is a 5 length vector
        data.append(row)


seed(1) # seed rand # generator
#w = [random() for i in range(4)]
#theta = 0
alpha = 0.08
y = []
yd = []

class neuron:
    def __init__(self, dSize, inputData):
        self.dSize = dSize
        self.weights = []
        #self.weights = []
        self.theta = random()
        
    def initWeights(self):
        for i in range(self.dSize):
            self.weights.append(random())

    def returnWeight(self, weight_num):
        w = weight_num
        return self.weights[w]

    def feedForward(self, inputData):
        dataRow = inputData
        guess = 0
        aggregation = 0
        data = dataRow[:self.dSize]
        
        for x in range(len(data)):
            point = data[x]
            wx = self.weights[x]
            aggregation += wx * float(point)
            aggregation = aggregation - self.theta
            guess = (1/(1+math.exp(-aggregation)))
        
        return guess
    
    def updateOWeights(self, D):
        delta = D
        for w in range(len(self.weights)):
            weight = self.weights[w]
            weight = weight + alpha * (y[w-3]) * delta
        self.theta = self.theta + alpha * -1 * delta

    def updateHWeights(self, D):
        for w in rage(len(self.weights)):
            




class layer: 

    def __init__(self, lSize, sSize, inputData):
        self.lSize = lSize
        self.sSize = sSize
        self.inputData = inputData
        self.n = []
        self.oDelta = []
        self.hDelta = []
        self.prevWeights = []

    def appendYd(self):
        actual = self.inputData[self.sSize:]
        for i in range(len(actual)):
            yd.append(float(actual[i]))

    def createNeurons(self):
        for x in range(self.lSize):
            self.n.append(neuron(self.sSize, self.inputData))
        for x in range(self.lSize):
            self.n[x].initWeights()

    def forward(self):
        for j in range(self.lSize):
            y.append(self.n[j].feedForward(self.inputData))

    def calcOdeltas(self):
        y.reverse()
        self.n.reverse()
        yd.reverse()
        yOut = self.n[:self.lSize]
        
        for i in range(len(yOut)):
            newODelta = (y[i] * (1-y[i]) * (yd[i]-y[i]))
            self.oDelta.append(newODelta)
        
        for d in range(len(self.oDelta)):
            self.n[d].updateOWeights(self.oDelta[d])
    
    def calcHdeltas(self):
        yHidden = self.n[self.lSize:]
        
        for i in range(len(yHidden)):
            newHDelta = (y[i] * (1 - y[i]) * ((self.oDelta[i]*self.n[1].weights[i]) + (self.oDelta[i+1]*self.n[2].weights[i]) + (self.oDelta[i+2]*self.n[3].weights[i])))
            self.hDelta.append(newHDelta)

        for d in range(len(self.hDelta)):
            self.n[d].updateHWeights(self.hDelta[d])


# TO DO:
#
#       figure out why each neuron initializes too many weights ---DONE
#
#       pass each layer's neurons and thier weights into something global
#       in order to be able to pass values between layers
#       currently, each layer's neurons are unable to pass data back and forth.



#main body

for epoch in range(1):
    
    for sample in data:    

        #hidden layer definition
        hidden = layer(3, 4, sample)    
        hidden.createNeurons()
        
        hidden.forward()
        hidden.appendYd()

        #output layer definition
        output = layer(3, 3, y)
        output.createNeurons()
        output.forward()

        output.calcOdeltas()
        hidden.calcHdeltas()

        #clear out y and yd after operating on each sample row in the data
        #print(hidden.delta)
        #print(". . . . . . . . . . .")
        #print(output.delta)
    #print(hidden.n[1].weights)
    