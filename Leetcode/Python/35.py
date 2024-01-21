
nums=[1,3,5,6]
target = 7

def searchInsert(nums,target):
    if target in nums:
        return nums.index(target)
    else:
        nums.append(target)
        sor = nums.sort()
        return nums.index(target)


print(searchInsert(nums,target))
