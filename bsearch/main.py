# -*- coding: utf-8 -*-
# @Time    : 2022/10/4 19:54
# @Author  : zhujiyuan

from matplotlib import pyplot as plt
import random

def getTestSet():
    x = list(range(100))
    y = [random.randint(0,130) for i in range(100)]
    y.sort()
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
    plt.pause(0.5)


obj_goal = 71
print(f"obj={obj_goal}")
l = 0
r = len(xs)-1

while l<=r:
    mid = int((l + r) / 2)
    if ys[mid]==obj_goal:
        print(f"successful! index = {mid},v = {ys[mid]}")

        plotBar(mid)

        break
    if obj_goal>ys[mid]:
        l = mid+1
    else:
        r = mid-1

    plotBar(mid)

if l>r:
    print(f"fail! ")
plt.show()


