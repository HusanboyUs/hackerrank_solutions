s='   -42'

def myAtoi(s: str):
    result = []
    sample = [str(x) for x in range(0,10)]
    for ele in s:
        if ele in sample:
            result.append(ele)

    final = ''.join(result)
    return int(final)      


print(myAtoi(s))    