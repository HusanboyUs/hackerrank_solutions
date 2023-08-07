class Solution:
    def firstUniqChar(self, s: str) -> int:
        for i,c in enumerate(s):
            if s.count(c)==1:
                return i
                break
        return -1
    #please upvote me it would encourage me alot