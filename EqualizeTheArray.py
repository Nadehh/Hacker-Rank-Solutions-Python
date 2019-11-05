#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the equalizeArray function below.
def equalizeArray(arr):
    seen_before = dict()
    max_count = 0

    for item in arr:
        try:
            seen_before[item] +=1
        except KeyError:
            seen_before[item] = 1
            
        if seen_before[item] > max_count:
            max_count = seen_before[item]
    
    return len(arr) - max_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
