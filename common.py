#capitalize challange
import os

def solve(s):
    lst = [v.capitalize() for v in s.split(' ')]
    result = ' '.join(lst)
    return result  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()