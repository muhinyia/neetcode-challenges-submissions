class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) == 1:
            return [strs]
        strSet = {}
        for string in strs:
            sorted_string = "".join(sorted(string))
            if sorted_string in strSet:
                strSet[sorted_string].append(string)
            else:
                strSet[sorted_string] =[string]

        return list(strSet.values())
