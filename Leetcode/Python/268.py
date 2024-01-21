
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = []
        for x in range(0,len(nums)):
            if x not in nums:
                res.append(x)

        if len(nums) not in res:
            res.append(len(nums))        
        return res[0]     