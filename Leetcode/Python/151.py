class Solution:
    def reverseWords(self, s: str) -> str:
        first = list(s.split())[::-1]
        return ' '.join(first)