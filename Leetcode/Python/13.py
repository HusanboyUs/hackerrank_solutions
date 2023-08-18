
s='III'

def romanToInt(s:str):
    roman_dict={
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
    }
    result=[]
    for st in s:
        for val,ky in roman_dict.items():
            if st == val:
                result.append(ky)

    return sum(result)               

print(romanToInt(s))    