import numpy
import pandas

def ave(x):
    num = len(x)
    sum0 = 0
    for i in range(num):
        sum0 = sum0 + x[i]
    return (sum0 / num)

def std(x):
    num = len(x)
    a = ave(x)
    s = 0
    for i in range(num):
        s = s + (a - x[i])**2 / num
    s = s ** 0.5
    return s

def norm(x):
    a = ave(x)
    s = std(x)
    l = []
    for i in range(len(x)):
        l.append((x[i] - a) / s)
    return l

data = pandas.read_csv("Salary_Data.csv")

Xreal = data.values[:,0]
Yreal = data.values[:,1]
m = len(Xreal)

aveX = ave(Xreal)
stdX = std(Xreal)
aveY = ave(Yreal)
stdY = std(Yreal)

Xnorm = norm(Xreal)
Ynorm = norm(Yreal)
Xnorm = numpy.expand_dims(Xnorm,1)
Xnorm = numpy.transpose(Xnorm)
Xnorm = numpy.concatenate([numpy.ones((1, len(Xreal))), Xnorm], axis=0)
Ynorm = numpy.expand_dims(Ynorm,1)
Ynorm = numpy.transpose(Ynorm)

theta = numpy.array([[0],[0]])
lr = 0.1
epochs = 1000

for epoch in range(epochs):
    temp = numpy.transpose(numpy.matmul(numpy.transpose(theta) , Xnorm) - Ynorm)
    theta = theta - (lr/m) * numpy.matmul(Xnorm , temp)

theta[1,0] = theta[1,0] * (stdY / stdX)
theta[0,0] = aveY + stdY * theta[0,0] - theta[1,0] * aveX

while True:
    n = float(input("Enter a number: "))
    result = theta[0,0] + n * theta[1,0]
    print(f"{n}: {result}")