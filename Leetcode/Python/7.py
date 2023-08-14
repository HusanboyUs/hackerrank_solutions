x = 1534236469
Output = -321


def reverseInterger(x):
    res = []
    if len(list(str(x)))  > 10:
        for ele in str(x)[::-1]:
            if ele.isdigit():
                res.append(ele)
        for x in str(x):
            if not x.isdigit():
                res.insert(0,x)    

        return ''.join(res)  
    return 0     


print(reverseInterger(x))    