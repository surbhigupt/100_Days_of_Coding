#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr = [0 for i in range(n+1)]
    
    for x, y, z in queries:
        arr[x-1] += z
        arr[y] -= z
     
    arr_max = 0
    cum_sum = arr[0]
    for x in range(1, len(arr)):
        cum_sum = cum_sum + arr[x]
        if cum_sum>arr_max:
            arr_max = cum_sum
        else:
            continue
        
    return arr_max

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
