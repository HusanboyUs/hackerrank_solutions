
nums=[7,8,3,5,2,6,3,1,1,4,5,4,8,7,2,0,9,9,0,5,7,1,6]

def smallestEqual(nums):
    res = []
    for x in range(len(nums)):
        if x%10 == nums[x]:
            res.append(x)

    if len(res) !=0:
        return sorted(res)[0]
    else:
        return -1           
          

print(smallestEqual(nums))    