#!/usr/bin/python
# coding:utf-8
import numpy as np
from matplotlib import pyplot as plt

step = 0
color = {1:[0,0,0],2:[255,255,255]}

def check(playground, point):
    available = False
    x,y = point
    # hengxiang
    
def show(playground):
    _ = [[100,100,100],[80,100,120]] * 4
    __ = [[80,100,120],[100,100,100]] * 4
    background = np.array((_ + __)*4).reshape((8,8,3))
    for i in range(8):
        for j in range(8):
            if playground[i][j]>0:
                background[i,j] = color[playground[i][j]]
    ax.imshow(background)
    fig.canvas.draw()

def on_press(event):
    global step,color
    
    # ax.imshow(background)
    
    if event.button==1:
        # print(round(float(event.ydata)),round(float(event.xdata)))
        if not playground[round(float(event.ydata))][round(float(event.xdata))] == 0:
            return
        playground[round(float(event.ydata))][round(float(event.xdata))] = step % 2 + 1
        show(playground)
        fig.canvas.draw()
        step += 1
    if step == 60:
        print("Over")

if __name__ == "__main__":
    playground = [
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,1,2,0,0,0],
        [0,0,0,2,1,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
    ]
    fig = plt.figure()
    fig.canvas.mpl_connect("button_press_event", on_press)
    ax = fig.add_subplot(111)
    show(playground)
    plt.axis("off")
    plt.show()