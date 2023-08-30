class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #li = s.strip().split(" ")
        #ans = len(li[-1])
        #return ans
        return len(s.strip().split()[-1])
