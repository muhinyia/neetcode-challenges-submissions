class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
            tempHolder = {}
            for char in s:
                if char in tempHolder:
                    tempHolder[char.lower()] += 1
                else:
                    tempHolder[char.lower()] = 1

            for char in t:
                if char.lower() not in tempHolder:
                    return False
                else:
                    if tempHolder[char.lower()] == 1:
                        tempHolder.pop(char.lower())
                    else:
                        tempHolder[char.lower()] -= 1

        return tempHolder == {}

                    

         