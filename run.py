#!/usr/bin/python
# coding:utf-8
import copy
import numpy as np
from matplotlib import pyplot as plt

def line_change(playground, x, y, player):
    temp = copy.deepcopy(playground)
    # 向左
    if y >= 2:
        temp[x][y] = player
        for i in range(1,y):
            if i == 1:
                if playground[x][y-1] == player * -1:
                    temp[x][y-1] = player
                else:
                    break
            else:
                if playground[x][y-i] == player * -1:
                    temp[x][y-i] = player
                elif playground[x][y-i] == player:
                    playground = temp
                else:
                    break
    temp = copy.deepcopy(playground)
    # 向右
    if y <= playground.shape[1] - 3:
        temp[x][y] = player
        for i in range(1,playground.shape[1] - y + 1):
            if i == 1:
                if playground[x][y+1] == player * -1:
                    temp[x][y+1] = player
                else:
                    break
            else:
                if playground[x][y+i] == player * -1:
                    temp[x][y+i] = player
                elif playground[x][y+i] == player:
                    playground = temp
                else:
                    break
    return playground

def row_change(playground, x, y, player):
    temp = copy.deepcopy(playground)
    # 向左
    if x >= 2:
        temp[x][y] = player
        for i in range(1,x):
            if i == 1:
                if playground[x-1][y] == player * -1:
                    temp[x-1][y] = player
                else:
                    break
            else:
                if playground[x-i][y] == player * -1:
                    temp[x-i][y] = player
                elif playground[x-i][y] == player:
                    playground = temp
                else:
                    break
    temp = copy.deepcopy(playground)
    # 向右
    if x <= playground.shape[0] - 3:
        temp[x][y] = player
        for i in range(1,playground.shape[0] - x + 1):
            if i == 1:
                if playground[x+1][y] == player * -1:
                    temp[x+1][y] = player
                else:
                    break
            else:
                if playground[x+i][y] == player * -1:
                    temp[x+i][y] = player
                elif playground[x+i][y] == player:
                    playground = temp
                else:
                    break
    return playground

def check(line, index, player):
    l = len(line)
    if index == 0:
        if not line[1] == player * -1:
            return False
        for i in range(l-2):
            if line[i+2] == player:
                return True
            elif line[i+2] == player * -1:
                continue
            elif line[i+2] == 0:
                return False
        else:
            return False
    elif index == l - 1:
        if not line[l-2] == player * -1:
            return False
        for i in range(l-2):
            if line[l-3-i] == player:
                return True
            elif line[l-3-i] == player * -1:
                continue
            elif line[l-3-i] == 0:
                return False
    else:
        pass
        
class PlayGround:
    def __init__(self):
        # player = 1 or -1
        self.player = 1
        self.color = {1:[0,0,0],-1:[0,255,255]}
        self.playground = [
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,-1,0,0,0],
            [0,0,0,-1,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ]
    def img(self):
        _ = [[100,100,100],[50,100,150]] * 4
        __ = [[50,100,150],[100,100,100]] * 4
        background = np.array((_ + __)*4).reshape((8,8,3))
        for i in range(8):
            for j in range(8):
                if self.playground[i][j]>0:
                    background[i,j] = self.color[self.playground[i][j]]
        return background
    def show(self):
        background = self.img()
        plt.imshow(background)
        plt.axis()
        plt.show()
    def check(self, location):
        if self.playground[location[0]][location[1]] > 0:
            return False
        else:
    def play(self, location):
        fig = plt.figure()
        fig.canvas.mpl_connect("button_press_event", on_press)
        ax = fig.add_subplot(111)
        show(self.playground)
        plt.axis()
        # plt.grid()
        plt.show()

    

def neighbor(x,y,playground):
    # 左上角(0,0)
    if x == 0:
        if y == 0:
            return [(0,1),(1,0),(1,1)]
        elif y == 7:
            return [(0,6),(1,7),(1,6)]
        else:
            return [(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]
    elif x == 7:
        if y == 0:
            return [(7,1),(6,0),(6,1)]
        elif y == 7:
            return [(7,6),(6,7),(6,6)]
        else:
            return [(x,y-1),(x,y+1),(x-1,y-1),(x-1,y),(x-1,y+1)]
    else:
        if y == 0:
            return [(x-1,0),(x-1,1),(x,1),(x+1,0),(x+1,1)]
        elif y == 7:
            return [(x-1,7),(x-1,6),(x,6),(x+1,6),(x+1,7)]
        else:
            return [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]

def get_possible_location(playground):
    res = []
    for i in range(8):
        for j in range(8):
            pass
    
def show(playground):
    _ = [[100,100,100],[50,100,150]] * 4
    __ = [[50,100,150],[100,100,100]] * 4
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
        playground[round(float(event.ydata))][round(float(event.xdata))] = player
        show(playground)
        fig.canvas.draw()
        player = player * -1
    # if step == 60:
        # print("Over")

if __name__ == "__main__":
    playground = make_playground()
    fig = plt.figure()
    fig.canvas.mpl_connect("button_press_event", on_press)
    ax = fig.add_subplot(111)
    show(playground)
    plt.axis()
    # plt.grid()
    plt.show()