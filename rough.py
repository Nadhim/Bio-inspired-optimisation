import math
import matplotlib.pyplot as plt

def delta_process(W,data):
    s=0
    for i in range(len(W)):
        s+= W[i]*data[i]
    
    w_sum =s

    sigmoid = 1/(1 + (math.exp(-w_sum))) 
    error = data[-1] - sigmoid
    delta = sigmoid*(1-sigmoid)*error

    return delta,error



# W = [0.3897, -0.3658, 0.7690] #Inital Weights
W = [0.3897] #Inital Weights

# dataset =[[0,0,1,0],
#     [0,1,1,0],
#     [1,0,1,1],
#     [1,1,1,1]]

dataset =[[0,1],
    [1,0]]


a = 0.9

x_values =[]
w1_values =[]
w2_values =[]
w3_values =[]
mse =[]
for _ in range(500):
    x_values.append(_)
    e=0
    for i in range(len(dataset)):
        d=delta_process(W,dataset[i])
        e+= d[0]**2

        W[0] += a*d[0]*dataset[i][0]
        # W[1] += a*d[0]*dataset[i][1]
        # W[2] += a*d[0]*dataset[i][2]
    print(W)
    w1_values.append(W[0])
    # w2_values.append(W[1])
    # w3_values.append(W[2])
    mse.append(e)

plt.plot(x_values,w1_values,color='green')
# plt.plot(x_values,w2_values,color='blue')
# plt.plot(x_values,w3_values,color='red')
plt.grid()
plt.show()

plt.figure()
plt.scatter(x_values,mse)
plt.grid()
plt.show()



#000,010,100,110
#001,101,011,111