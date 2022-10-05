# -*- coding: utf-8 -*-
# @Time    : 2022/10/5 21:50
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
    plt.pause(0.1)

ts = ys.copy()
cnt = 0

def merge_sort(left,right):
    if left>=right:
        return None
    mid = int((left+right)/2)
    merge_sort(left,mid)
    merge_sort(mid+1,right)
    merge(left,mid,right)

def merge(left,mid,right):

    l = left
    r = mid+1
    tempArr = []
    while l<=mid and r<=right:
        if ys[l]<ys[r]:
            tempArr.append(ys[l])
            l+=1
        else:
            tempArr.append(ys[r])
            r+=1
    #merge other
    while l<=mid:
        tempArr.append(ys[l])
        l+=1
    while r<=right:
        tempArr.append(ys[r])
        r+=1

    #tempArr to ys
    for i in range(left,right+1):
        ys[i]=tempArr[i-left]
    plotBar()


merge_sort(0,len(ys)-1)

print(ys)

plt.show()
print(ys)
ts.sort()

for i in zip(ys,ts):
    if i[0]!=i[1]:
        print("false!!")
        break