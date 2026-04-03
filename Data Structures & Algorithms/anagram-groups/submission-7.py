class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashMap = {}
        for st in strs:
            this_string = "".join(x for x in sorted(st))
            if this_string in hashMap:
                hashMap[this_string].append(st)
            else:
                hashMap[this_string] = [st]
        return [x for x in hashMap.values()]