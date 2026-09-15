import numpy
X = numpy.array([1,2,3,4,5,6,7,8,9])
Y = numpy.array([2,6,7,10,14,16,20,23,26])

theta0 = 0
theta1 = 0

lr = 0.05
m = len(X)
epochs = 5000

for epoch in range(epochs):
    sum0 = 0
    sum1 = 0

    for i in range(m):
        sum0 = sum0 + (theta0 + theta1*X[i] - Y[i])
        sum1 = sum1 + (theta0 + theta1*X[i] - Y[i]) * X[i]

    theta0 = theta0 - (lr/m)*sum0
    theta1 = theta1 - (lr/m)*sum1

print(theta0,theta1)