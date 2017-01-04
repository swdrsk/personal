#coding:utf-8

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy

WALL = -2 # static
EMPTY = -1 # static
AMEBA = 20.0 # dynamic
FEED = 100 # static

colors = {
    "EMPTY":(1, 1, 1),
    "WALL":(0, 0, 0),
    "FEED":(0, 1, 0),
    "AMEBA":(1, 0.8, 0.2),
}
symbols = {
    "$":WALL,
    " ":AMEBA,
    "s":FEED,
    "t":FEED,
}
stagefile = "stage.txt"


def stage2colors(stage):
    colormap = deepcopy(stage)
    for i in range(len(stage)):
        for j in range(len(stage[0])):
            if stage[i][j] == EMPTY:
                colormap[i][j] = colors["EMPTY"]
            elif stage[i][j] == WALL:
                colormap[i][j] = colors["WALL"]
            elif stage[i][j] == FEED:
                colormap[i][j] = colors["FEED"]
            else:
                colormap[i][j] = (1, stage[i][j]/100, 0)
    return colormap

def update(stage):
    next_stage = deepcopy(stage)
    for i in range(1,len(stage)-1):
        for j in range(1,len(stage)-1):
            next_stage[i][j] = cell_rule(stage, i, j)
    return next_stage

def cell_rule(stage, i, j):
    result = stage[i][j]
    if stage[i][j] not in (WALL, EMPTY, FEED):
        around_walls = 0
        around_cells = 0
        for x,y in [(-1,0),(1,0),(0,-1),(0,1)]:
            if stage[i+x][j+y] in [WALL, EMPTY]:
                around_walls += 1
            elif stage[i+x][j+y] > stage[i][j]:
                around_cells += 1
                stage[i][j] += 0.2*(stage[i+x][j+y] - stage[i][j]) - 1
                if around_cells > 2:
                    stage[i][j] = EMPTY
        result = stage[i][j] if around_walls < 3 else EMPTY
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
for t in range(100):
    stage = update(stage)
    im = plt.imshow(stage2colors(stage), interpolation='none')
    ims.append([im])
ani = animation.ArtistAnimation(fig,ims)
plt.show()
