# -*- coding: utf-8 -*-
# @Time    : 2022/10/5 19:16
# @Author  : zhujiyuan
from matplotlib import pyplot as plt
import random

def getTestSet():
    x = list(range(100))
    y = [random.randint(0,300) for i in range(100)]

    return x,y

#get test set
xs,ys = getTestSet()
print(ys)
def plotBar(cur,min_index):
    plt.clf()
    plt.xlim(0,105)
    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))

    plt.bar(xs,ys)
    plt.bar([cur],[ys[cur]],color='r')
    plt.bar([min_index], [ys[min_index]], color='black')
    plt.pause(0.5)

ts = ys.copy()
cnt = 0


for i in range(len(ys)):
    min_index = i
    for j in range(i,len(ys)):

        if ys[j]<ys[min_index]:
            min_index = j

            cnt += 1
            if cnt%4==0:
                plotBar(i, min_index)

    ys[i],ys[min_index]=ys[min_index],ys[i]
    plotBar(i, min_index)


plt.show()
print(ys)
ts.sort()

for i in zip(ys,ts):
    if i[0]!=i[1]:
        print("false!!")
        break