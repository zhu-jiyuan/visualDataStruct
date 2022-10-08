# -*- coding: utf-8 -*-
# @Time    : 2022/10/5 22:07
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
def plotBar():
    plt.clf()
    plt.xlim(0,105)

    plt.gca().xaxis.set_major_locator(plt.MultipleLocator(5))

    plt.bar(xs,ys)
    plt.pause(0.5)

ts = ys.copy()
cnt = 0


def count_sort():
    #init 10 list
    #keyword is 3

    buckets = [[] for i in range(10)]

    for i in range(3):
        #sort with keyword to bucket
        for num in ys:
            buckets[int(num/(10**i))%10].append(num)


        #recycle
        index = 0
        for bucket in  buckets:
            for v in bucket:
                #print(f"index={index},v={v}")
                ys[index]=v
                #
                index+=1
            plotBar()
        buckets = [[] for i in range(10)]
        #plotBar()
count_sort()


plt.show()
print(ys)
ts.sort()

for i in zip(ys,ts):
    if i[0]!=i[1]:
        print("false!!")
        break