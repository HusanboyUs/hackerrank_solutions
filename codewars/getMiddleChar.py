word='testing'

def findMiddle(s):
    if len(s) > 2:
        if len(s) % 2 ==0:
            len_div=len(s) // 2
            print(s[len_div-1]+s[len_div])
        elif len(s) % 2 !=0:
            print(s[len(s)//2])    
    else:
        print(s)          


findMiddle(word)

'''
def get_middle(s):
    if len(s) > 2:
        if len(s)%2 == 0:
            len_div=len(s) // 2
            return s[len_div-1]+s[len_div]
        elif len(s)%2!=0:
            return s[len(s)//2] 
        
    else:
        return s
'''
