#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternatingCharacters function below.
def alternatingCharacters(a):
    string_list = [a[0]]
    del_cnt = 0
    for i in range(1, len(a)):
        if a[i]==string_list[-1]:
            del_cnt += 1
            continue
        else:
            string_list.append(a[i])
        
    return del_cnt

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = alternatingCharacters(s)

        fptr.write(str(result) + '\n')

    fptr.close()
