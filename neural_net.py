#coding;utf-8
import numpy as np
import matplotlib.pyplot as plt
import pdb


class Layer(object):
    def __init__(self,pre,post):
        self.pre = np.zeros(pre)
        self.post = np.zeros(post)
        self.thre = np.random.rand(pre) - 0.5
        self.weight = self.init_weight(post, pre)

    def init_weight(self, post, pre):
        return np.random.random([post, pre])*2 - 1

    def activation(self, inputs):
        sigmoid = 1/(1+np.exp(-inputs))
        tanh = np.tanh(-inputs)
        relu = np.array(map(lambda x:(0 if x<0 else x), inputs))
        return sigmoid

    def inv_activation(self, inputs):
        sigmoid = inputs*(1-inputs)
        return sigmoid

    def out(self,inputs):
        # output = np.dot(self.weight,self.activation(inputs))+self.thre
        output = self.activation(np.dot(self.weight,inputs+self.thre))
        return output

    def learn(self,err,learning_rate):
        for i,invpre in enumerate(self.inv_activation(self.pre)):
            self.weight[:,i] += learning_rate*err*self.post*invpre
        # return np.dot(np.linalg.pinv(self.weight), err)*self.inv_activation(self.pre)
        return np.dot(self.weight.T, err)

    def plearn(self,err,learning_rate):
        self.weight = self.init_weight(len(self.post),len(self.pre))
        return err

class NeuralNet(object):
    def __init__(self,*nums):
        self.layer = []
        for pre,post in zip(nums[:-1],nums[1:]):
            self.layer.append(Layer(pre,post))
        
    def fit(self,inputsignal,outputsignal,learning_rate):
        if inputsignal.shape[1] != len(self.layer[0].pre):
            print("mismatch input dim vs. units num")
        if outputsignal.shape[1] != len(self.layer[-1].post):
            print("mismatch output dim vs. units num")
        if inputsignal.shape[0] != outputsignal.shape[0]:
            print("mismatch input length and output length")
        err = 0
        for signal,teacher in zip(inputsignal,outputsignal):
            output = self.feedforward(signal)
            self.learn(output-teacher, learning_rate)
            err = output-teacher
        return err
                        
    def learn(self,err,learning_rate=0.01):
        for layer in self.layer[::-1]:
            err = layer.learn(err, learning_rate)

    def feedforward(self, inputsignal):
        isignal = inputsignal
        osignal = 0
        for layer in self.layer:
            osignal = layer.out(isignal)
            isignal = osignal
        return osignal

    def predict(self, inputsignals):
        output = np.zeros([len(inputsignals),len(self.layer[-1].post)])
        for i,inputsignal in enumerate(inputsignals):
            output[i,:] = self.feedforward(inputsignal)
        return output
            

def run():
    def class_func(x):
        return 0.01*(x+1)*(x-8)*(x-7)

    def classify(x):
        return x[1] > class_func(x[0])

    input_signal = np.random.random([100,2])*20 - 10
    output_signal = np.zeros(100)
    for i in range(100):
        output_signal[i] = classify(input_signal[i]).astype(int)
    output_signal = output_signal.reshape([len(output_signal),1]) # need to reshape
    test_signal = np.random.random([50,2]) * 20 - 10
    NN = NeuralNet(2,3,1)
    for i in np.arange(1,10,0.1):
        err = NN.fit(input_signal, output_signal, learning_rate=0.1/i)
        print err
    predict = NN.predict(test_signal)
    plt.figure()
    for data in zip(test_signal, predict):
        plt.scatter(*data[0], color="r" if data[1] > 0.5 else "b")
    if False:
        plt.figure()
        for data in zip(input_signal, output_signal):
            plt.scatter(*data[0], color="y" if data[1] > 0.5 else "g")
        plt.plot(np.arange(-10, 10, 0.1), class_func(np.arange(-10, 10, 0.1)))
    plt.show()


def test():
    L1 = Layer(2,3)
    inputsignal = np.random.random(2)
    print L1.out(inputsignal)
    NN = NeuralNet(2,3,1)
    print NN.feedforward(inputsignal)

if __name__=="__main__":
    run()
