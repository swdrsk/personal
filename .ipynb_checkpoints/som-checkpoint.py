import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

row = 40
col = 40
learntime = 100000
alpha = 0.05
weight = np.random.random([row,col,3])

def som(colorvec):
    min_index = np.argmin(((weight-colorvec)**2).sum(axis=2))
    mini = int(min_index / col)
    minj = int(min_index % col)
    weight[mini,minj] += 0.5 * alpha * (colorvec - weight[mini,minj])
    for i in range(-2,3):
        for j in range(-2,3):
            try:
                weight[mini+i,minj+j] += alpha * (colorvec - weight[mini+i,minj+j])/(abs(i)+abs(j)+1)
            except:
                pass

def show_rslt():
    im = plt.imshow(weight,interpolation='none')
    return im
    
fig = plt.figure()
plt.axis('off')
ims = []
for time in xrange(learntime):
    color = np.random.rand(3)
    som(color)
    if time % 500 == 0:
        ims.append([show_rslt()])
ani = animation.ArtistAnimation(fig, ims)
# ani.save('som.mp4') # <- NOT able to use on Windows
plt.show()