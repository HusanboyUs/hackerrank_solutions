class Solution:
    def sumOfMultiples(self, n: int) -> int:
        result =[]
        for i in range(1,n+1):
            if i%3 == 0 or i%5 ==0 or i%7==0:
                result.append(i)
        return sum(result)        
