import csv
from random import random
from random import seed

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
w = [random() for i in range(4)]
theta = 0
alpha = 0.1
for epoch in range(100):

    # init tally to 0
    tally = 0

    for sample in data:
        x = sample[:4]
        yd = sample[4]
        guess = 0
        aggregation = 0
        
        # aggregate sum of xi*wi-theta
        for i in range(4):
            xi = x[i]
            wi = w[i]
            aggregation += wi * float(xi)

        aggretation = aggregation - theta
        # assign guess value based on aggregation
        if aggregation <= 0:
            guess = -1
        
        elif aggregation > 0:
            guess = 1
        
        #compare guess value to yd
        if float(yd) != guess:
            tally += 1
            # error correction
            for j in range(4):
                wj = w[j]
                xj = x[j]
                w[j] = wj + alpha*float(xj)*(float(yd)-guess)
                theta = theta -alpha*-1*(float(yd)-guess)

    accuracy = (len(data)-tally) / len(data)
    print("epoch "+ str(epoch) +" accuracy: "+ str(accuracy))
        

