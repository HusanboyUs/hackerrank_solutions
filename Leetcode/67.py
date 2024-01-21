

a=11
b=1

def addBinary(a,b):
    return bin(int(a, 2) + int(b, 2))[2:]

print(addBinary(a,b))    