s = "hello"

def reverseVowels(s):
    index_vow=[]
    for indx,char in enumerate(list(s)):
        if char in ['a', 'e', 'i', 'o','u']:
            index_vow.append(indx)

    print(index_vow) 
   
    for i in index_vow[::-1]:
        for indx,char in enumerate(list(s)):
            if
    

print(reverseVowels(s))    