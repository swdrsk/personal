#coding:utf-8

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy

colors = {
    "empty":(1, 1, 1),
    "wall":(0, 0, 0),
    "feed":(1, 0, 0),
    "ameba":(1, 0.8, 0.2),
}
symbols = {
    "$":"wall",
    " ":"ameba",
    "s":"feed",
    "t":"feed",
}
stagefile = "stage.txt"


def stage2colors(stage):
    colormap = deepcopy(stage)
    for i in range(len(stage)):
        for j in range(len(stage[0])):
            colormap[i][j] = colors[stage[i][j]]
    return colormap

def update(stage):
    next_stage = deepcopy(stage)
    for i in range(1,len(stage)-1):
        for j in range(1,len(stage)-1):
            next_stage[i][j] = cell_rule(stage, i, j)
    return next_stage

def cell_rule(stage, i, j):
    result = stage[i][j]
    if stage[i][j] == "ameba":
        around_cells = 0
        for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
            if stage[i+x][j+y] in ["ameba","feed"]:
                around_cells += 1
        result = "ameba" if around_cells > 1 else "empty"
    return result

f = open(stagefile,"r")
lines = f.readlines()
stage = []
for line in lines:
    line = line.replace("\n","")
    line = line.replace("\r","")
    stage.append([symbols[i] for i in line])
# stage = np.array(stage)

"""
for t in range(30):
    stage = update(stage)
plt.axis("off")
plt.imshow(stage2colors(stage), interpolation='none')
plt.show()

"""
ims = []
fig = plt.figure()
plt.axis('off')
for t in range(40):
    stage = update(stage)
    im = plt.imshow(stage2colors(stage), interpolation='none')
    ims.append([im])
ani = animation.ArtistAnimation(fig,ims)
plt.show()


