
num = 8

def mySqrt(num):
    return num//2

#print(mySqrt(num))    


'''
nums = [2,7,8,5]

def checkDuplicate(nums):
    return len(nums) == len(set(nums))
        
print(checkDuplicate(nums))

'''

word = 'aslan'


def wordly(word):
    low,high = 0,len(word)-1

    while low < high:
        if word[low] != word[high]:
            return False
        else:
            low +=1
            high-=1
        return True

print(wordly(word))