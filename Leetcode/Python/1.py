class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result = []
        for leader in range(len(nums)):
            for follower in range(leader +1,len(nums)):
                if nums[leader] + nums[follower] == target:
                    result.append(leader)
                    result.append(follower)
        return result      
