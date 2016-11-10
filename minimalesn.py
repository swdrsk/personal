#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt


def twoneuron(W,randominit=False):
    duration = 100000
    neurons = np.array([0.5,0.5])
    state = np.zeros([2,duration])
    thre = np.random.random(2)
    if randominit:
        neurons = np.random.random(2)
    state[:,0] = neurons
    for dt in range(1,duration):
        neurons += (-neurons + np.dot(W,np.tanh(neurons - thre)))/100
        state[:,dt] = neurons
    plt.plot(*state)

def test():
    W = np.array([[1,2],[2,1]])/3
    twoneuron(W)
    plt.show()
    
    
if __name__=="__main__":
    test()
