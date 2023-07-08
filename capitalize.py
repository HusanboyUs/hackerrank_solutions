letter='1 w 2 r 3g'
result=[]
print(letter.split())
for i in letter.split():
    if i.isnumeric():
       result.append(i)
       print(i)
    else:    
        result.append(i.title())
        print(i)

print(''.join(result))
