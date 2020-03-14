#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    
    nb = (bin(n))


    max_ones = max(nb[2:].split('0')) #"11" for eg 13 (as split two 11,1 )

    count_one = max_ones.count('1') # how many 1 two

    print(count_one)
