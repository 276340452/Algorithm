#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import random
import time
import math
import sys

def swap(arr, i, j):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def main():
  # sys.setrecursionlimit(1000000)  # 设置最大递归深度
  N = eval(input('请输入N（N为正整数）：'))
  arr = []
  i = 0
  while i < N:
    arr.append(int(random.uniform(1,50000)))
    i = i + 1
  start = time.process_time()
  # BubbleSort(arr)
  # SelectionSort(arr)
  # InsertionSort(arr)
  # ShellSort(arr)
  # arr = MergeSort(arr)
  QuickSort(arr,0,len(arr)-1)
  end = time.process_time()
  print(arr)
  k = int(N/2)
  print('当N=%d时排序花费时间为：%s,k=%s' % (N,end - start,arr[k]))

# 快速排序
def QuickSort(arr,left,right):
  if left < right:
    partitionIndex = partition(arr,left,right)
    QuickSort(arr,left,partitionIndex-1)
    QuickSort(arr,partitionIndex+1,right)
def partition(arr,left,right):
  pivot = left
  index = pivot + 1
  i = index
  while i <= right:
    if arr[i] < arr[pivot]:
      swap(arr,i,index)
      index = index + 1
    i = i + 1
  swap(arr,pivot,index-1)
  return index-1

# 归并排序
def MergeSort(arr):
  if len(arr)<2:
    return arr
  # 切换分为两个数组
  middle = math.floor(len(arr)/2)
  left = arr[0:middle]
  right = arr[middle:len(arr)]
  # 递归调用归并算法
  return merge(MergeSort(left),MergeSort(right))
def merge(left,right):
  result = []
  while len(left)>0 and len(right)>0:
    # 比较大小，依次放入数组
    if left[0] < right[0]:
      result.append(left.pop(0))
    else:
      result.append(right.pop(0))
  # 将剩余数组放入数组
  while len(left):
    result.append(left.pop(0))
  while len(right):
    result.append(right.pop(0))
  return result

# 希尔排序（缩小增量排序）
def ShellSort(arr):
  gap = 1
  # 动态设置增量
  while gap < len(arr):
    gap = gap * 3 + 1
  
  while gap > 0:
    i = gap
    # 插入排序
    while i < len(arr):
      current = arr[i]
      prePos = i - gap
      while prePos >= 0 and arr[prePos] > current:
        arr[prePos + gap] = arr[prePos]
        prePos = prePos - gap
      arr[prePos + gap] = current
      i = i + 1
    # 动态设置增量
    gap = math.floor(gap/3)

# 插入排序
def InsertionSort(arr):
  i = 0
  while i < len(arr):
    # 记录当前值
    current = arr[i]
    # 前一个值的位置
    prePos = i - 1
    # 依次与前一个值对比，直到比当前值小的位置
    while prePos >= 0 and arr[prePos] > current:
      arr[prePos + 1] = arr[prePos]
      prePos = prePos - 1
    # 插入
    arr[prePos + 1] = current
    i = i + 1

# 选择排序
def SelectionSort(arr):
  i = 0
  left = 0
  right = len(arr)-1
  # 确定未排序的数据段
  while left < right:
    minPos = left
    maxPos = right
    i = left
    while i <= right:
      # 记录最小值的位置
      if arr[i] > arr[maxPos]:
        maxPos = i
      # 记录最大值的位置
      if arr[i] < arr[minPos]:
        minPos = i
      i = i + 1
    # 交换
    swap(arr,left,minPos)
    # temp = arr[left]
    # arr[left] = arr[minPos]
    # arr[minPos] = temp
    swap(arr,right,maxPos)
    # temp = arr[right]
    # arr[right] = arr[maxPos]
    # arr[maxPos] = temp
    left = left + 1
    right = right - 1

# 冒泡排序
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
        swap(arr,j,j-1)
        # temp = arr[j]
        # arr[j] = arr[j-1]
        # arr[j-1] = temp
        flag = 1
        posMin = j # 记录最后一次交换的位置
      j = j - 1
    if flag == 0: #如果一次循环没有交换，已排序
      return
    n = posMin
    i = i + 1

main()
