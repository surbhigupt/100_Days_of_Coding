#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    
    multiplier = n//len(s)
    remainder = n%len(s)
    
    count_a = 0
    count_a = count_a + sum([1 for i in s if i=='a'])*multiplier
    count_a = count_a + sum([1 for i in range(remainder) if s[i]=='a'])
    
    return count_a

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
