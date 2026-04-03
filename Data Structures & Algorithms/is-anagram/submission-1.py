class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False
        countS = {}
        countT = {}
        for idx in range(len(s)):
            countS[s[idx]] = 1 + countS.get(s[idx], 0)
            countT[t[idx]] = 1 + countT.get(t[idx], 0)
        return countS == countT