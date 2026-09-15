X = [1,2,3,4,5,6,7,8,9,10]
Y = [106,207,303,405,498,595,703,803,909,997]

theta0 = 0
theta1 = 0

learning_rate = 0.001
num_x = len(X)
repeat_num = 10000

for repeat in range(repeat_num):

    sum0 = 0
    sum1 = 0

    for i in range(num_x):
        sum0 = sum0 + (theta0 + theta1*X[i] - Y[i])
        sum1 = sum1 + (theta0 + theta1*X[i] - Y[i]) * X[i]

    theta0 = theta0 - (learning_rate/num_x)*sum0
    theta1 = theta1 - (learning_rate/num_x)*sum1

print(theta0,theta1)