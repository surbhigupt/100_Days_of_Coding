#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the stringReduction function below.
def stringReduction(s):
    s_counter = Counter(s)
    alpha_count = sum([v%2 for k, v in s_counter.items()])
    if len(s_counter)==1:
        return len(s)
    elif alpha_count==0 or (alpha_count//2==1 and alpha_count%2==1):
        return 2
    else:
        return 1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = stringReduction(s)

        fptr.write(str(result) + '\n')

    fptr.close()
