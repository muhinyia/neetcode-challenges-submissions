class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d_d = defaultdict(list)

        for s in strs:
            s_sorted = "".join(sorted(s))
            d_d[s_sorted].append(s)
        
        return list(d_d.values())


        