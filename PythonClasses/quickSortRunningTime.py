import math
import os
import random
import re
import sys
import time

# Complete the quickSort function below.


def quicksort(ar):
    n = len(ar)
    p = ar[0]
    lt = []  # less than(lt)
    gt = []  # greater than(gt)
    et = []  # equal to(et)
    for i in range(0, n, 1):
        if ar[i] > p:
            gt.append(ar[i])
        elif ar[i] < p:
            lt.append(ar[i])
        else:
            et.append(ar[i])
        # recursion starts here
        if len(lt) > 1:
            lt = quicksort(lt)
            print(' '.join(map(str, lt)))
        if len(gt) > 1:
            gt = quicksort(gt)
            print(' '.join(map(str, gt)))
        if len(et) > 1:
            et = quicksort(et)
            print(' '.join(map(str, et)))

    return lt + et + gt


def main():
    input()
    arr = list(map(int, input().strip().split()))
    startTime = time.time()
    result = quicksort(arr)
    timeOfExecution = time.time() - startTime
    print(' '.join(map(str, result)))
    print("Execution time = {}".format(timeOfExecution))


main()