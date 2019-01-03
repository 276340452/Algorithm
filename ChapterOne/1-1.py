#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time

def main():
  N = eval(input('请输入N（N为正整数）：'))
  arr = []
  i = 0
  while i < N:
    arr.append(int(random.uniform(1,50000)))
    i = i + 1
  start = time.process_time()
  BubbleSort(arr)
  end = time.process_time()
  print(arr)
  k = int(N/2)
  print('当N=%d时排序花费时间为：%s,k=%s' % (N,end - start,arr[k]))

def BubbleSort(arr):
  i = 0
  posMax = 0 # 最后一次交换位置
  posMin = 0 # 最后一次交换位置
  k = len(arr)-1 # 最后一次最大交换位置
  n = 0 # 最后一次最小交换位置
  while i<len(arr)-1:
    j = 0
    flag = 0 # 标记
    # 最大
    j = n
    while j<k:
      # 交换
      if arr[j] > arr[j+1]:
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
        flag = 1 # 标记交换
        posMax = j # 标记最后一次交换的位置
      j = j + 1
    if flag == 0: # 如果一次循环没有交换，已排序
      return
    k = posMax
    # 最小
    j = k
    while j > n:
      # 交换
      if arr[j] < arr[j-1]:
        temp = arr[j]
        arr[j] = arr[j-1]
        arr[j-1] = temp
        flag = 1
        posMin = j # 记录最后一次交换的位置
      j = j - 1
    if flag == 0: #如果一次循环没有交换，已排序
      return
    n = posMin
    i = i + 1
main()
