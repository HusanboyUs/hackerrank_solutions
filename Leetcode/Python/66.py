class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digit = ''.join(map(str,digits))
        digit_add = int(digit) +1
        res= [int(x) for x in str(digit_add)]
        return res