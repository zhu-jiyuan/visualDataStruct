# -*- coding: utf-8 -*-
# @Time    : 2022/10/4 21:57
# @Author  : zhujiyuan

from matplotlib import pyplot as plt
import random

def getTestSet():
    x = list(range(100))
    y = [random.randint(0,300) for i in range(100)]

    return x,y

#get test set
xs,ys = getTestSet()

def plotBar():
    plt.clf()
    plt.xlim(0,105)

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))

    plt.bar(xs,ys)
    plt.pause(0.1)

cnt = 0
for i in range(len(xs)-1):
    for j in range(len(xs)-1-i):
        if ys[j]>ys[j+1]:
            ys[j],ys[j+1] = ys[j+1],ys[j]
        #speed x 20
        cnt+=1
        if cnt%20==0:
            plotBar()

plt.show()

print(ys)