#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#


def diagonalDifference(arr):
    x_sum = 0
    y_sum = 0
    for i in range(len(arr)):
        x_sum += arr[i][i]

    for i in range(len(arr)):
        y_sum += arr[i][len(arr)-1-i]

    return [(x_sum-y_sum) if x_sum > y_sum else (y_sum-x_sum)][0]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
