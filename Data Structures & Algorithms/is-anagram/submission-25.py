class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMap = {}
        for char in s:
            if char in hashMap:
                hashMap[char] += 1
            else:
                hashMap[char] = 1

        for char in t:
            if char not in hashMap:
                return False
            else:
                if hashMap[char] == 1:
                    hashMap.pop(char)
                else:
                    hashMap[char] -= 1
        return len(hashMap)==0