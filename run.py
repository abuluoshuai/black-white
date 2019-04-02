#!/usr/bin/python
# coding:utf-8
import sys
import copy
import random
import numpy as np
from matplotlib import pyplot as plt
 
class PlayGround:
    def __init__(self):
        # player = 1 or -1
        self.player = 1
        self.step = 0
        self.status = True
        self.color = {1:[0,0,0],-1:[255,255,255]}
        self.playground = np.array([
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,1,-1,0,0,0],
            [0,0,0,-1,1,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0],
        ])
    def img(self):
        _ = [[0,255,255],[0,128,0]] * 4
        __ = [[0,128,0],[0,255,255]] * 4
        background = np.array((_ + __)*4).reshape((8,8,3))
        for i in range(8):
            for j in range(8):
                if self.playground[i][j] != 0:
                    background[i][j] = self.color[self.playground[i][j]]
        return background
    def show(self):
        background = self.img()
        plt.imshow(background)
        plt.axis()
        plt.show()
    def line_change(self, playground, location):
        x,y = location
        # 向左
        temp = copy.deepcopy(playground)
        if y >= 2:
            temp[x][y] = self.player
            for i in range(1,y):
                if i == 1:
                    if playground[x][y-1] == self.player * -1:
                        temp[x][y-1] = self.player
                    else:
                        break
                else:
                    if playground[x][y-i] == self.player * -1:
                        temp[x][y-i] = self.player
                    elif playground[x][y-i] == self.player:
                        playground = temp
                    else:
                        break
        # 向右
        temp = copy.deepcopy(playground)
        if y <= playground.shape[1] - 3:
            temp[x][y] = self.player
            for i in range(1,playground.shape[1] - y):
                if i == 1:
                    if playground[x][y+1] == self.player * -1:
                        temp[x][y+1] = self.player
                    else:
                        break
                else:
                    if playground[x][y+i] == self.player * -1:
                        temp[x][y+i] = self.player
                    elif playground[x][y+i] == self.player:
                        playground = temp
                    else:
                        break
        return playground
    def row_change(self, playground, location):
        x,y = location
        # 向上
        temp = copy.deepcopy(playground)
        if x >= 2:
            temp[x][y] = self.player
            for i in range(1,x):
                if i == 1:
                    if playground[x-1][y] == self.player * -1:
                        temp[x-1][y] = self.player
                    else:
                        break
                else:
                    if playground[x-i][y] == self.player * -1:
                        temp[x-i][y] = self.player
                    elif playground[x-i][y] == self.player:
                        playground = temp
                    else:
                        break
        # 向下
        temp = copy.deepcopy(playground)
        if x <= playground.shape[0] - 3:
            temp[x][y] = self.player
            for i in range(1,playground.shape[0] - x):
                if i == 1:
                    if playground[x+1][y] == self.player * -1:
                        temp[x+1][y] = self.player
                    else:
                        break
                else:
                    if playground[x+i][y] == self.player * -1:
                        temp[x+i][y] = self.player
                    elif playground[x+i][y] == self.player:
                        playground = temp
                    else:
                        break
        return playground
    def diagonal_change(self, playground, location):
        x,y = location
        # 左上
        temp = copy.deepcopy(playground)
        if x >= 2 and y >= 2:
            temp[x][y] = self.player
            for i in range(1,min(x,y)):
                if i == 1:
                    if playground[x-1][y-1] == self.player * -1:
                        temp[x-1][y-1] = self.player
                    else:
                        break
                else:
                    if playground[x-i][y-i] == self.player * -1:
                        temp[x-i][y-i] = self.player
                    elif playground[x-i][y-i] == self.player:
                        playground = temp
                    else:
                        break
        # 右下
        temp = copy.deepcopy(playground)
        if x <= playground.shape[0] - 3 and y <= playground.shape[1] - 3:
            temp[x][y] = self.player
            for i in range(1,min(playground.shape[0] - x, playground.shape[1] - y)):
                if i == 1:
                    if playground[x+1][y+1] == self.player * -1:
                        temp[x+1][y+1] = self.player
                    else:
                        break
                else:
                    if playground[x+i][y+i] == self.player * -1:
                        temp[x+i][y+i] = self.player
                    elif playground[x+i][y+i] == self.player:
                        playground = temp
                    else:
                        break
        # 右上
        temp = copy.deepcopy(playground)
        if x >= 2 and y >= 2 and y <= 6:
            temp[x][y] = self.player
            for i in range(1,min(x,playground.shape[1] - y)):
                if i == 1:
                    if playground[x-1][y+1] == self.player * -1:
                        temp[x-1][y+1] = self.player
                    else:
                        break
                else:
                    if playground[x-i][y+i] == self.player * -1:
                        temp[x-i][y+i] = self.player
                    elif playground[x-i][y+i] == self.player:
                        playground = temp
                    else:
                        break
        # 左下
        temp = copy.deepcopy(playground)
        if x <= playground.shape[0] - 3 and y <= playground.shape[1] - 3:
            temp[x][y] = self.player
            for i in range(1,min(playground.shape[0] - x, y)):
                if i == 1:
                    if playground[x+1][y-1] == self.player * -1:
                        temp[x+1][y-1] = self.player
                    else:
                        break
                else:
                    if playground[x+i][y-i] == self.player * -1:
                        temp[x+i][y-i] = self.player
                    elif playground[x+i][y-i] == self.player:
                        playground = temp
                    else:
                        break
        return playground
    def check(self, location):
        res = False
        if not self.playground[location[0]][location[1]] == 0:
            return res
        else:
            if not (self.playground == self.line_change(self.playground, location)).all():
                res = True
            elif not (self.playground == self.row_change(self.playground, location)).all():
                res = True
            elif not (self.playground == self.diagonal_change(self.playground, location)).all():
                res = True
        return res
    def get_possible_location(self):
        res = []
        for i in range(self.playground.shape[0]):
            for j in range(self.playground.shape[1]):
                if self.check((i,j)):
                    res.append((i,j))
        return res
    def get_status(self):
        if not self.get_possible_location():
            self.status = False
            print(self.player)
            print(self.playground.sum())
            print(self.playground)
    def random(self):
        possible_locations = self.get_possible_location()
        step = random.choice(possible_locations)
        self.play(step)
        print(self.step,step)
    def random_play(self):
        while self.status:
            self.random()
    def play(self, location):
        if self.check(location):
            self.playground = self.line_change(self.playground, location)
            self.playground = self.row_change(self.playground, location)
            self.playground = self.diagonal_change(self.playground, location)
            self.player = self.player * -1
            self.step += 1
            self.get_status()
            return True
        return False

def on_press(event):
    global pg
    if event.button==1:
        location = [round(float(event.ydata)), round(float(event.xdata))]
        pg.play(location)
        ax.imshow(pg.img())
        fig.canvas.draw()

if __name__ == "__main__":
    pg = PlayGround()
    if len(sys.argv)>1:
        if sys.argv[1] == "2":
            fig = plt.figure()
            fig.canvas.mpl_connect("button_press_event", on_press)
            ax = fig.add_subplot(111)
            ax.imshow(pg.img())
            plt.axis()
            plt.show()
        if sys.argv[1] == "random":
            pg.random_play()
            pg.show()
