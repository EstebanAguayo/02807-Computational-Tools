import sys
import numpy as np
import matplotlib.pyplot as plt
from numba import njit
import time


start_time = time.time()

def sum(n):
    res = 0
    for i in range(1, n):
        res += 1/(i**2)
    return res

@njit
def numbaSum(n):
    res = 0
    for i in range(1, n):
        res += 1/(i**2)
    return res

if __name__ == "__main__":
    start = time.perf_counter()                         #Time start

    n = int(sys.argv[1])                                   # The first argument, sys.argv[0] is the name of the file...
    sel = sys.argv[2]

    iter = 2000

    if sel == 1:
        for i in range(iter):
            res = sum(n)
    else:
        for i in range(iter):
            res = numbaSum(n)

    end = time.perf_counter()
    print("Standard way result %s, time %.7f" %(res, end-start))