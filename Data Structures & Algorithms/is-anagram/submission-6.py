class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            hashMap = {}
            # construct hashmap
            for char in s:
                if char in hashMap:
                    hashMap[char] += 1
                else:
                    hashMap[char] = 1
                    
            # deconstruct hashmap heart earth
            for c in t:
                if c not in hashMap:
                    return False
                else:
                    if hashMap[c]>1:
                        hashMap[c] -= 1
                    else:
                        hashMap.pop(c)
        return len(hashMap) == 0