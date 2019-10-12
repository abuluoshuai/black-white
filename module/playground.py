#!/usr/bin/python
# coding:utf-8
import sys
import copy
import random
import numpy as np
from PIL import Image,ImageDraw
import matplotlib.pyplot as plt

class PlayGround:
    def __init__(self, edge = 50, color1 = (255,153,18), color2 = (118,128,105), color3 = (255,0,0)):
        # player = 1 or -1
        self.player = 1
        self.edge = edge
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.step = 0
        self.status = True
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
        self.pg_img = self.basicImg()
    def basicImg(self):
        e = Image.new('RGB',(self.edge * 8,self.edge * 8),(255,255,255))
        c1 = Image.new('RGB',(self.edge,self.edge),self.color1)
        c2 = Image.new('RGB',(self.edge,self.edge),self.color2)
        for i in range(8):
            for j in range(8):
                if i % 2 == 0:
                    if j % 2 == 0:
                        e.paste(c1, (i*self.edge, j*self.edge, i*self.edge+self.edge,j*self.edge+self.edge))
                    else:
                        e.paste(c2, (i*self.edge, j*self.edge, i*self.edge+self.edge,j*self.edge+self.edge))
                else:
                    if j % 2 == 0:
                        e.paste(c2, (i*self.edge, j*self.edge, i*self.edge+self.edge,j*self.edge+self.edge))
                    else:
                        e.paste(c1, (i*self.edge, j*self.edge, i*self.edge+self.edge,j*self.edge+self.edge))
        return e
    def img(self):
        im = self.pg_img.copy()
        draw = ImageDraw.Draw(im)
        for i in range(8):
            for j in range(8):
                if self.playground[i][j] == 1:
                    draw.ellipse(((i+0.1)*self.edge,(j+0.1)*self.edge,(i-0.1)*self.edge+self.edge,(j-0.1)*self.edge+self.edge),fill = "black")
                elif self.playground[i][j] == -1:
                    draw.ellipse(((i+0.1)*self.edge,(j+0.1)*self.edge,(i-0.1)*self.edge+self.edge,(j-0.1)*self.edge+self.edge),fill = "white")
                elif self.check((i,j)):
                    draw.ellipse(((i+0.1)*self.edge,(j+0.1)*self.edge,(i-0.1)*self.edge+self.edge,(j-0.1)*self.edge+self.edge),fill = self.color3)
        return im
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
            for i in range(1,y+1):
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
            for i in range(1,x+1):
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
            for i in range(1,min(x+1,y+1)):
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
        if x >= 2 and y <= playground.shape[1] - 3:
            temp[x][y] = self.player
            for i in range(1,min(x+1,playground.shape[1] - y)):
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
        if x <= playground.shape[0] - 3 and y >= 2:
            temp[x][y] = self.player
            for i in range(1,min(playground.shape[0] - x, y+1)):
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
            #print(self.player)
            # _ = self.result()
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
    def result(self):
        if not self.status:
            s = self.playground.sum()
            if s > 0:
                print(u"黑胜！")
                return 1
            elif s < 0:
                print(u"白胜！")
                return -1
            else:
                print(u"平局！")
                return 0