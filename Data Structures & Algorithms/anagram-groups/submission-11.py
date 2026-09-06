class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashSet = {}

        for st in strs:
            sortedSt = "".join(sorted(st))
            if sortedSt in hashSet:
                hashSet[sortedSt].append(st)
            else:
                hashSet[sortedSt] = [st]
        return list(hashSet.values())