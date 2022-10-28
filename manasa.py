#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'stones' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER a
#  3. INTEGER b
#
from itertools import permutations
def stones(n, a, b):
    r = []
    
    
    if a >b:
        a, b = b, a
    gap = b-a
    v1 = a*(n-1)
    r.append(v1)
    if gap==0:
        return r
    
    for i in range(1,n):
        r.append(v1 + (i*gap))
        #r.append(r[-1]+gap)
    return r
        

    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
