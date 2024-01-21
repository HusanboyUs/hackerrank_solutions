nums= [1,2,4,5,6,7,8,9]

result=[]

index = 0
for x in nums:
    if index %2 ==0 and x %2 ==0:
        result.append(x)
    index +=1   
        

print(result)            

result=[]

for ind,char in enumerate(nums):
    if ind % 2 ==0 and char %2==0:
        result.append(char)

print(result)        
