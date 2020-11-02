#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    arr_set = list(set(ar))
    arr2 = []
    for i in arr_set:
        arr_count = 0
        for j in ar:
            if i == j:
                arr_count = arr_count + 1
            else:
                continue
        arr2 = arr2 + [arr_count//2]
    return sum(arr2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
