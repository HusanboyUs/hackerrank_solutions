
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    
binary = ""

while n > 0:
    binary = str(n % 2) + binary
    n = int(n / 2)

print(max([item for item in binary.split("0")]).count("1"))