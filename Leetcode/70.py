
n=2
def climbStairs(n):
    result = 0
    while result !=n:
        for x in range(0,n):
            result +=x
    return result

print(climbStairs(n))    