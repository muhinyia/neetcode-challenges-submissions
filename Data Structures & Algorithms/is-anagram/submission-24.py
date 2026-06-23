class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hashSet = {}
        for char in s:
            if char in hashSet:
                hashSet[char] += 1 
            else:
                hashSet[char] = 1
        for char in t:
            if char not in hashSet:
                return False
            else:
                if hashSet[char] == 1:
                    hashSet.pop(char)
                else:
                    hashSet[char] -= 1
       
        return not bool(hashSet)
