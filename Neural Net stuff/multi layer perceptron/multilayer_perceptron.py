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
        #self.weights = [random() for i in range(self.dSize)]
        self.weights = []
        self.theta = random()
        

    def calcWeights(self):
        for i in range(self.dSize):
            self.weights[i].append(random())
        return self.weights

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
    
    def updateWeights(self, delta):
        self.delta = delta
        for w in range(len(self.weights)):
            weight = self.weights[w]
            #weight = (weight + 'y1'alpha * delta)




class layer: 

    def __init__(self, lSize, sSize, inputData):
        self.lSize = lSize
        self.sSize = sSize
        self.inputData = inputData
        self.n = []
        self.delta = []
        self.nWeights = []

    def appendYd(self):
        actual = self.inputData[self.sSize:]
        for i in range(len(actual)):
            yd.append(float(actual[i]))

    def createNeurons(self):
        for x in range(self.lSize):
            self.n.append(neuron(self.sSize, self.inputData))

    def grabWeights(self):
        for wSet in self.n:
            self.nWeights.append(self.n[wSet].calcWeights())
        print(self.nWeights)
            


    def passSample(self):
        for j in range(self.lSize):
            #y.clear()
            y.append(self.n[j].feedForward(self.inputData))

    def calcOdeltas(self):
        y.reverse()
        self.n.reverse()
        yd.reverse()
        yOut = self.n[:self.lSize]
        
        for i in range(len(yOut)):
            newDelta = (y[i] * (1-y[i]) * yd[i])
            self.delta.append(newDelta)
        
        for w in range(len(self.delta)):
            self.n[i].updateWeights(self.delta[w])
    
    def calcHdeltas(self):
        yHidden = self.n[self.lSize:]

        #for i in range(yHidden):
            #delta.append:(y[i]*)




#main body

for epoch in range(1):
    
    for sample in data:    

        #hidden layer definition
        hidden = layer(3, 4, sample)    
        hidden.grabWeights()
        hidden.createNeurons()
        hidden.passSample()
        hidden.appendYd()

        #output layer definition
        output = layer(3, 3, y)
        output.createNeurons()
        output.grabWeights()
        output.passSample()

        output.calcOdeltas()
        hidden.calcHdeltas()

        hidden.grabWeights()
        
        #clear out y and yd after operating on each sample row in the data
