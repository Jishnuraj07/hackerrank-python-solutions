#!/bin/python3
import math
import os
import random
import re
import sys

# Complete the bigSorting function below.
n = int(input().strip())
unsorted = []
unsorted_i = 0

for unsorted_i in range(n):
 unsorted_t = str(input().strip())
 unsorted.append(unsorted_t)
print('\n'.join(sorted(unsorted,key=int)))