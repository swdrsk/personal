#coding;utf-8
import numpy as np
import matplotlib.pyplot as plt
import pdb

class Layer(object):
    def __init__(self,pre,post):
        self.pre = np.zeros(pre)
        self.post = np.zeros(post)
        self.thre = np.random.rand(pre) - 0.5
        self.weight = self.init_weight(pre,post)

    def init_weight(self,pre,post):
        return np.random.random([post,pre]) - 0.5

    def activation(self,inputs):
        sigmoid = 1/(1+np.exp(-inputs))
        tanh = np.tanh(-inputs)
        relu = np.array(map(lambda x:(0 if x<0 else x), inputs))
        return sigmoid
        
    def out(self,inputs):
        # output = np.dot(self.weight,self.activation(inputs))+self.thre
        output = self.activation(np.dot(self.weight,inputs)+self.thre)
        return output

    def learn(self,err,learning_rate):
        self.weight += learning_rate*(self.post-err)*self.pre
        return np.dot(np.linalg.inv(self.weight),err)

class NeuralNet(object):
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
        if inputsignal.ndim != len(self.layer[0].pre):
            print("mismatch input dim vs. units num")
        if outputsignal.ndim != len(self.layer[-1].post):
            print("mismatch output dim vs. units num")
        if inputsignal.shape[1] != outputsignal.shape[1]:
            print("mismatch input length and output length")
        for signal,teacher in zip(inputsignal,outputsignal):
            output = self.feedforward(inputsignal)
            self.learn(teacher)
                        
    def learn(self,err):
        for layer in self.layer[::-1]:
            err = layer.learn(err)

    def feedforward(self,inputsignal):
        isignal = inputsignal
        for layer in self.layer:
            osignal = layer.out(isignal)
            isignal = osignal
        return osignal

    def predict(self,inputsignals):
        output = np.zeros([len(inputsignals),len(self.layer[-1].post)])
        for i,inputsignal in enumerate(inputsignals):
            output[i,:] = feedforward(inputsignal)
            

def run():
    def classify(x):
        return x[1] > 0.01*(x[0]+1)*(x[0]-8)*(x[0]+7)
    input_signal = np.random.random([2,100])*10 - 5
    output_signal = classify(input_signal).astype(int)
    test_signal = np.random.random([2,50]) * 10 -5
    NN = NeuralNet(2,3,1)
    NN.fit(input_signal,output_signal)
    predict = NN.predict(test_signal)
    for t,p in zip(test_signal,predict):
        plt.plot(*t,colar="r" if predict[0] else "b")
    plt.show()

def test():
    L1 = Layer(2,3)
    inputsignal = np.random.random(2)
    print L1.out(inputsignal)

if __name__=="__main__":
    test()
