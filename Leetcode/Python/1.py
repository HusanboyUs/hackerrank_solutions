nums = [2,7,11,15]
target = 9
result=[]



lead = 1
while lead != len(nums):
    for x in range(len(nums)):
        total = nums[x] + nums[lead]
        print(total)
        result.append(total)
    lead +=1

print(result)    