#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    
    def string_dict_func(string):
        string_dict = {}
        for i in string:
            string_dict[i] = sum([1 for j in string if j==i])
        return string_dict
    
    dict_a = string_dict_func(a)
    dict_b = string_dict_func(b)
    
    d = {k:dict_a.get(k, 0)-dict_b.get(k,0) for k in dict_a.keys()|dict_b.keys()}
    
    return sum(abs(i) for i in d.values())

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
