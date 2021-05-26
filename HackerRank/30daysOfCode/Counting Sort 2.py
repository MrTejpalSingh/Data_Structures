#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def countingSort(arr):
    freq_arr = [0 for i in range(100)]
    for i in arr:
        if i <= 100:
            freq_arr[i] += 1
    sorted_list = []
    for i in range(100):
        if i == 0 and freq_arr[i] == 0:
            continue
        if freq_arr[i] == i:
            sorted_list.append(i)
        else:
            for j in range(freq_arr[i]):
                sorted_list.append(i)
    return sorted_list

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#     n = int(input().strip())
#
#     arr = list(map(int, input().rstrip().split()))
#
#     result = countingSort(arr)
#
#     fptr.write(' '.join(map(str, result)))
#     fptr.write('\n')
#
#     fptr.close()
