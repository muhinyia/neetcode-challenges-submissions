class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <=1:
            return [strs]
        else:
            hashMap = {}
            for word in strs:
                sortedWord = str(sorted(word))
                if sortedWord in hashMap:
                    hashMap[sortedWord].append(word)
                else:
                    hashMap[sortedWord] = [word]
                    
        return list(hashMap.values())