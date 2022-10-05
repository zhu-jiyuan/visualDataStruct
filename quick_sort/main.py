# -*- coding: utf-8 -*-
# @Time    : 2022/10/4 22:31
# @Author  : zhujiyuan
# ref:https://www.programiz.com/dsa/quick-sort
from matplotlib import pyplot as plt
import random

def getTestSet():
    x = list(range(100))
    y = [random.randint(0,300) for i in range(100)]

    return x,y

#get test set
xs,ys = getTestSet()
print(ys)
def plotBar():
    plt.clf()
    plt.xlim(0,105)

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))

    plt.bar(xs,ys)
    plt.pause(0.1)

ts = ys.copy()
cnt = 0

def qSort(left,right):
    global cnt
    if left>=right:
        return None


    base = ys[right]
    second = left
    cur = left
    while cur<right:
        if ys[cur]<base:
            ys[second],ys[cur]=ys[cur],ys[second]
            second+=1
        cur+=1

        #speed x10
        cnt = cnt+1
        if cnt%10==0:
            plotBar()
    ys[second], ys[right] = ys[right], ys[second]
    plotBar()
    qSort(left,second-1)
    qSort(second+1,right)
qSort(0,len(ys)-1)

plt.show()
print(ys)
ts.sort()

for i in zip(ys,ts):
    if i[0]!=i[1]:
        print("false!!")
        break