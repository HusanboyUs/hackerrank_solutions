class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        resultBin = []
        resultGarbage = []

        for x in nums:
            if x not in resultBin:
                resultBin.append(x)
            else:
                resultGarbage.append(x)

        result = None
        for x in nums:
            if x  not in resultGarbage:
                result =x

        return result    