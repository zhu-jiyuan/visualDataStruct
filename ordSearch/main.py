# -*- coding: utf-8 -*-
# @Time    : 2022/10/4 21:39
# @Author  : zhujiyuan

from matplotlib import pyplot as plt
import random

def getTestSet():
    x = list(range(100))
    y = [random.randint(0,130) for i in range(100)]

    return x,y

#get test set
xs,ys = getTestSet()

def plotBar(mid):
    plt.clf()
    plt.xlim(0,105)
    plt.ylim(0,150)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))

    plt.bar(xs,ys)
    plt.bar([mid],[ys[mid]],color='r')
    plt.pause(0.1)

obj_goal = 55

for i in xs:
    if ys[i]==obj_goal:
        plotBar(i)
        print(f"successful! index = {i},v = {ys[i]}")
        break
    plotBar(i)
plt.show()