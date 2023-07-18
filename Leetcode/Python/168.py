letters= ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

columnNumber = 28
result = []


if columnNumber >= 27:
    for indx, x in enumerate(letters,start=1):
        for n in str(columnNumber):
            if indx == int(n):
                result.append(x)   

else:
    for indx,x in enumerate(letters,start=1):
        if indx == columnNumber:
            result.append(x)

print(result)            

