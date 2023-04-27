
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())

if N%2!=0:
    print('Weird')
elif N%2==0 and N in [i for i in range(2,5)]:
    print('Not Weird')
elif N%2==0 and N in [i for i in range(6,21)]:
    print('Weird') 
elif N>20:
    print('Not Weird')    
        