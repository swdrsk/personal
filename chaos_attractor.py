#coding:utf-8
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import pdb


class Attractor:
    def __init__(self):
        self.dt = 0.01
        self.x = 0.1
        self.y = 0.1
        self.z = 0.1
        self.output = []

    def initialize(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def run(self,T):
        for t in range(T):
            self.step()
            self.output.append([self.x,self.y,self.z])
        return self.output

    def step(self):
        return self.x,self.y,self.z

    def draw(self,display=True,plotfig=None):
        if not self.output:
            print("not run...do Lorents.run(T=t)")
            return 0
        if display:
            fig = plt.figure()
            ax = fig.gca(projection='3d')
            ax.plot(*zip(*self.output))
            plt.show()
        else:
            try:
                plotfig.plot(*zip(*self.output))
            except:
                print("draw Error...")
                print("USAGE: draw(display=False,plotfig=<object plt.figure().gca>)")


class Lorenz(Attractor):
    def __init__(self,p,r,b):
        # p=10,r=28,b=8/3 in Lorenz(1963)        
        Attractor.__init__(self)
        self.p = float(p)
        self.r = float(r)
        self.b = float(b)

    def step(self):
        x,y,z = self.x,self.y,self.z
        self.x += self.dt*(-self.p*(x-y))
        self.y += self.dt*(-x*z + self.r*x - y)
        self.z += self.dt*(x*y - self.b*z)
        return self.x, self.y, self.z


class Rossler(Attractor):
    def __init__(self,a,b,c):
        # a=0.2,b=0.2,c=5.7 in Rossler(1976)
        Attractor.__init__(self)
        self.a = a
        self.b = b
        self.c = c

    def step(self):
        x,y,z = self.x,self.y,self.z
        self.x += self.dt*(-y-z)
        self.y += self.dt*(x+self.a*y)
        self.z += self.dt*(self.b+x*z-self.c*z)
        return self.x, self.y, self.z


if __name__=="__main__":
    fig = plt.figure(figsize=plt.figaspect(2.))
    ax = fig.add_subplot(2,1,1,projection="3d")
    la = Lorenz(10,28,8.0/3)
    la.run(10000)
    la.draw(display=False,plotfig=ax)
    ax2 = fig.add_subplot(2,1,2,projection="3d")
    rl = Rossler(0.2,0.2,5.7)
    rl.run(100000)
    rl.draw(display=False,plotfig=ax2)
    plt.show()
