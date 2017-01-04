import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import seaborn as sns
sns.set_style("whitegrid")

class ComplexSystem(object):
    def __init__(self, N):
        self.N = N
        self.field = [0,0,1000,1000]
        self.pos = np.random.random([2, N]) * 1000
        self.vel = np.random.random([2, N]) * 5
        self.orbit = []
        
    def update_pos(self):
        self.pos += self.vel
        for i in range(2):
            self.vel[i][np.where((self.pos[i] < self.field[i])|(self.pos[i] > self.field[i+2]))] *= -1
        self.pos += self.vel
        
    def run(self, time):
        self.orbit = np.zeros([time, 2, self.N])
        for t in range(time):
            self.update_pos()
            self.orbit[t,:,:] = self.pos
        
    def show_animation(self):
        fig = plt.figure()
        ims = []
        for t in range(len(self.orbit)):
            im = plt.scatter(*self.orbit[t,:,:])
            ims.append([im])
        ani = animation.ArtistAnimation(fig, ims, interval=50)
        plt.show()    
        
if __name__=="__main__":
    cs = ComplexSystem(20)
    cs.run(1000)
    cs.show_animation()