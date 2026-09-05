class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashSetS = {}
        hashSetT = {}

        for i in s:
            if i in hashSetS:
                hashSetS[i] += 1
            else:
                hashSetS[i] = 1

        for i in t:
            if i in hashSetT:
                hashSetT[i] += 1
            else:
                hashSetT[i] = 1

        for key in hashSetS:
            if key not in hashSetT:
                return False
            if hashSetS[key] != hashSetT[key]:
                return False
        return True
