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
alpha = 0.1
y = []
yd = []

class neuron:
    def __init__(self, dSize):
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
            oWeight = self.weights[w]
            oWeight = oWeight + alpha * (y[w-3]) * delta
        self.theta = self.theta + alpha * -1 * delta

    def updateHWeights(self, D, row):
        delta = D
        sRow = row
        for w in range(len(self.weights)):
            hWeight = self.weights[w]
            hWeight = hWeight + alpha *(float(sRow[w]))
        self.theta = self.theta + alpha * -1 * delta




class layer: 

    def __init__(self, lSize, sSize):
        self.lSize = lSize
        self.sSize = sSize
        self.n = []
        self.oDelta = []
        self.hDelta = []

    def appendYd(self, sample):
        sampleRow = sample
        actual = sample[self.sSize:]
        for i in range(len(actual)):
            yd.append(float(actual[i]))
        
    def createNeurons(self):
        for x in range(self.lSize):
            self.n.append(neuron(self.sSize))
        for x in range(self.lSize):
            self.n[x].initWeights()

    def forward(self, sample):
        sampleRow = sample
        for j in range(self.lSize):
            y.append(self.n[j].feedForward(sampleRow))

    #start backpropogation
    def calcOdeltas(self):
        y.reverse()
        #self.n.reverse()
        yd.reverse()
        yOut = len(self.n)
        
        for i in range(yOut):
            newODelta = (y[i] * (1-y[i]) * (yd[i]-y[i]))
            self.oDelta.append(newODelta)
        
        for d in range(len(self.oDelta)):
            self.n[d].updateOWeights(self.oDelta[d])
        
    
    def calcHdeltas(self, sample):
        yHidden = len(self.n)
        sRow = sample
        for i in range(yHidden):
            newHDelta = (y[i] * (1 - y[i]) * ((output.oDelta[0]*output.n[0].weights[i]) + (output.oDelta[1]*output.n[1].weights[i]) + (output.oDelta[2]*output.n[2].weights[i])))
            self.hDelta.append(newHDelta)

        for d in range(len(self.hDelta)):
            self.n[d].updateHWeights(self.hDelta[d], sRow)
        


# TO DO:
#
#       figure out why each neuron initializes too many weights --DONE
#
#       pass each layer's neurons and thier weights into something global
#       in order to be able to pass values between layers
#       currently, each layer's neurons are unable to pass data back and forth. -- ALTERNATIVE SOL. FOUND
#
#       figure out why MAD won't get smaller --Done



#main body

#hidden layer definition
hidden = layer(3, 4)    
hidden.createNeurons()
#output layer definition
output = layer(3, 3)
output.createNeurons()

for epoch in range(100):
    e = 0
    count = 0
    
    
    for sample in data:    

        hidden.forward(sample)
        hidden.appendYd(sample)

        output.forward(y)

        #calc deltas and update weights
        output.calcOdeltas()
        hidden.calcHdeltas(sample)
        
        
        output.oDelta.clear()
        hidden.hDelta.clear()
        
        #error sum for mad calc
        e += (abs(yd[0]-y[0]) + abs(yd[1]-y[1]) + abs(yd[2]-y[2])) 
        count += 1

        #clear out y and yd after operating on each sample row in the data
        
        yd.clear()
        y.clear()
    
    #calc MAD
    mad = (1/count) * e

    print("MAD: " + str(mad))
    