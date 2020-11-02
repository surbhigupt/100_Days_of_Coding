#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    cumulus = [i for i in range(n) if c[i]==0]
    shortest_path = [cumulus[0]]
    for i in range(1, len(cumulus)):
        if (shortest_path[-1] + 2) in cumulus:
            shortest_path = shortest_path + [(shortest_path[-1] + 2)]
        elif (shortest_path[-1] + 1) in cumulus:
            shortest_path = shortest_path + [(shortest_path[-1] + 1)]
    
    return (len(shortest_path)-1)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
