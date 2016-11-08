#coding;utf-8
import numpy as np
import matplotlib.pyplot as plt

class Layer:
    def __init__(self,pre,post):
        self.pre = pre
        self.post = post
        self.thre = np.random.rand(pre)
        self.weight = self.init_weight(pre,post)

    def activation(self,inputs):
        sigmoid = 1/1+np.exp(-inputs)
        tanh = np.tanh(-inputs)
        relu = np.array(map(lambda x:(0 if x<0 else x), inputs))
        return sigmoid
        
    def out(self,inputs):
        output = np.dot(self.weight*self.activation(inputs))+self.thre
        return output

    def learn(self,err):
        

class NeuralNet:
    def __init__(self,*nums):
        self.layer = []
        self.weight = []
        for i,num in enumerate(nums):
            self.layer[i] = Layer(num)
            if i>0:
                self.weight[i-1] = self.init_weight(pre_num,num)
            prenum = num

    def init_weight(x,y):
        return np.array.random.rand([pre_num,num])*2-1
        
    def fit(self,inputsignal,outputsignal):
        if inputsignal.ndim != self.layer[0].n:
            print("mismatch input dim vs. units num")
        if outputsignal.ndim != self.layer[-1].n:
            print("mismatch output dim vs. units num")
        if inputsignal.shape[1] != outputsignal.shape[1]:
            print("mismatch input length and output length")
        

    def predict(self,inputsignal):
        for insig in inputsignal:
            for layer in self.layer:
                layer.update[0]
