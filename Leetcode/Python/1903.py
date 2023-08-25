num ='35427'

def largestOddNumber(num):
    result = []
    for x in num:
        if int(x) %2!=0:
            result.append(x)


    return result        

print(largestOddNumber(num))      