#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the isValid function below.
def isValid(S):
    char_map = Counter(S)
    char_occurence_map = Counter(char_map.values())
 
    if len(char_occurence_map) == 1:
        return 'YES'
  
    if len(char_occurence_map) == 2:
        k1, k2 = char_occurence_map.keys()
        v1, v2 = char_occurence_map.values()
 
        # there is exactly 1 extra symbol and it can be deleted
        if (k1 == 1 and v1 == 1) or (k2 == 1 and v2 == 1):
            return 'YES'
 
        # the is exactly 1 symbol that occurs an extra 1 time
        if (k1 == k2+1 and v1 == 1) or (k2 == k1+1 and v2 == 1):
            return 'YES'
  
    return 'NO'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
