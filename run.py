#!/usr/bin/python
# coding:utf-8
import sys
import copy
import random
import numpy as np
from PIL import Image,ImageDraw
from matplotlib import pyplot as plt
from module import PlayGround

def random_play(pg):
    possible_locations = pg.get_possible_location()
    step = random.choice(possible_locations)
    pg.play(step)

def on_press(event):
    global pg,man_player
    # print(round(float(event.ydata)), round(float(event.xdata)))
    if event.button==1:
        location = [int(float(event.xdata)/50), int(float(event.ydata)/50)]
        if len(man_player) == 2:
            pg.play(location)
            ax.imshow(pg.img())
            fig.canvas.draw()
        else:
            if pg.play(location):
                random_play(pg)
                ax.imshow(pg.img())
                fig.canvas.draw()

if __name__ == "__main__":
    pg = PlayGround()
    if len(sys.argv)>1:
        # 2 man
        if sys.argv[1] == "2":
            man_player = [1,-1]
            fig = plt.figure()
            fig.canvas.mpl_connect("button_press_event", on_press)
            ax = fig.add_subplot(111)
            ax.imshow(pg.img())
            plt.axis()
            plt.show()
        # 2 random play
        elif sys.argv[1] == "random":
            while pg.status:
                random_play(pg)
            # pg.show()
            plt.imshow(pg.img())
            plt.show()
        # black is man, white is random
        elif sys.argv[1] == "1":
            man_player = [1]
            fig = plt.figure()
            fig.canvas.mpl_connect("button_press_event", on_press)
            ax = fig.add_subplot(111)
            ax.imshow(pg.img())
            plt.axis()
            plt.show()
        # black is random, white is man
        elif sys.argv[1] == "-1":
            man_player = [-1]
            fig = plt.figure()
            fig.canvas.mpl_connect("button_press_event", on_press)
            ax = fig.add_subplot(111)
            random_play(pg)
            ax.imshow(pg.img())
            plt.axis()
            plt.show()
        elif sys.argv[1] == "test":
            import time
            res = []
            start_time = time.time()
            for i in range(100000):
                pg = PlayGround()
                while pg.status:
                    random_play(pg)
                res.append(pg.playground.sum())
            end_time = time.time()
            black_win = sum([1 for i in res if i > 0])
            white_win = sum([1 for i in res if i < 0])
            ping = sum([1 for i in res if i == 0])
            print("B:%d\nW:%d\nP:%d"%(black_win, white_win, ping))
            print("Time spend:%d"%(end_time - start_time))