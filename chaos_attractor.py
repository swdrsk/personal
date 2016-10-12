#coding:utf-8

class Lorens:
    def __init__(self,p,r,b):
        # p=10,r=28,b=8/3 in Lorenz(1963)
        self.x = 0.1
        self.y = 0.1
        self.z = 0.1
        self.p = float(p)
        self.r = float(r)
        self.b = float(b)
        self.output = ()
    def initialize(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    def run(self,T):
        for t in range(T):
            self._step()
            self.output.append((self.x,self.y,self.z))
        return self.output
    def _step(self):
        x,y,z = self.x,self.y,self.z
        self.x = 
        self.y =
        self.z =
    def draw(self):
        if not output:
            print("not run...do Lorents.run(T=t)")
