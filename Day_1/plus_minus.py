#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#


def plusMinus(arr):
    arr_len = len(arr)
    plus_count = 0
    minus_count = 0
    zero_count = 0
    for i in arr:
        if i > 0:
            plus_count += 1
        if i < 0:
            minus_count += 1
        if i == 0:
            zero_count += 1
    plus_ratio = plus_count/arr_len
    minus_ratio = minus_count/arr_len
    zero_ratio = zero_count/arr_len
    print('%.6f' % plus_ratio, '\n%.6f' % minus_ratio, '\n%.6f' % zero_ratio)


if __name__ == '__main__':
    n = int(input().strip())
    '''
    # Sample Input
    STDIN           Function
    -----           --------
    6               arr[] size n = 6
    -4 3 -9 0 4 1   arr = [-4, 3, -9, 0, 4, 1]

    # Sample Output
    0.500000
    0.333333
    0.166667
    '''

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
