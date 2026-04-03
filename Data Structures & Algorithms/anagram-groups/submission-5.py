class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <=1:
            return [strs]
        else:
            hashMap = {}
            for word in strs:
                sortedWord = "".join(sorted(word))
                if sortedWord in hashMap:
                    hashMap[sortedWord].append(word)
                else:
                    hashMap[sortedWord] = [word]
        print(hashMap)            
        return list(hashMap.values())