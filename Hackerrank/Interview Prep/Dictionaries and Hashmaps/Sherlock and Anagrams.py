#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    x = []
    for i in range(1, len(s)):
        y = []
        for j in range(0, len(s)-i+1):
            y.append(''.join(sorted(s[j:j+i])))
        x = x+y
    count = Counter(x)

    output = 0
    for i in count.values():
        output += sum(range(i))
    
    return output
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
