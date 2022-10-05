# -*- coding: utf-8 -*-
# @Time    : 2022/10/5 16:35
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


print(ys)
ts = ys.copy()

cnt = 0
insert_i = 1
while insert_i<len(ys):
    cur = insert_i-1
    insert_v = ys[insert_i]
    while cur>=0:
        if insert_v<ys[cur]:
            ys[cur+1] = ys[cur]
        elif insert_v>=ys[cur]:
            ys[cur+1] = insert_v
            break
        cur=cur-1
        #speed x10
        cnt+=1
        if cnt%10==0:
            plotBar()
    if cur==-1:
        ys[0]=insert_v
    plotBar()

    insert_i=insert_i+1

plt.show()

print(ys)
print(ts)
ts.sort()

for i in zip(ys,ts):
    if i[0]!=i[1]:
        print("false!!")
        break




