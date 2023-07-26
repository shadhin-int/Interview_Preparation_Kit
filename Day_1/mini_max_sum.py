#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def miniMaxSum(arr):
    sorted_arr = sorted(arr)
    len_of = len(sorted_arr)
    min_sum = 0
    max_sum = 0

    for i in range(len_of):
        min_sum = sum(sorted_arr[:(len_of-1)])
        max_sum = sum(sorted_arr[1:len_of])

    print(min_sum, max_sum)


if __name__ == '__main__':
    '''
    the respective minimum and maximum values as a single line of two space-separated long integers
    # Sample Input
    1 2 3 4 5

    # Sample Output
    10 14
    '''

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
