#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(mag, note):
    
    mag_dict = Counter(mag)
    note_dict = Counter(note)

    output = 'Yes'
    for k, v in note_dict.items():
        if k in mag_dict and v<=mag_dict[k]:
            continue
        else:
            output = 'No'
            break
    
    return print(output)

if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
