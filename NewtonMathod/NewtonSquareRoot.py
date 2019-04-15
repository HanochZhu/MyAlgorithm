#!/usr/bin/env python
# coding=UTF-8
'''
@Description: use newton method to cal square root for n
@Author: thissky
@LastEditors: Please set LastEditors
@Date: 2019-04-15 14:46:11
@LastEditTime: 2019-04-15 17:18:36
'''

import cmath
import time
import math

def SquareRoot(n):
    tx = 100
    lstx = tx
    for i in range(10):
        tx = (n / tx / 2 + tx / 2)
        if (abs(tx - lstx) < 0.0000001):
            break
        lstx = tx
    return tx

n = 15
root = SquareRoot(n)
start = time.clock()
print(root)
end = time.clock()
print("newton method run time is {0}".format(end - start))
start = time.clock()
print(n ** 0.5)
end = time.clock()
print("power method run time is {0}".format(end - start))
start = time.clock()
print(cmath.sqrt(n))
end = time.clock()
print("cmath method run time is {0}".format(end - start))