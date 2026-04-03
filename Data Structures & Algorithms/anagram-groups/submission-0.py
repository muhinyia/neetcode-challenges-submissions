class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs)<1: return [[""]]
        else:
            grouped_strs = []
            for i in range(len(strs)):
                if strs[i] == None:
                    continue
                else:
                    this_group = [strs[i]]
                for j in range(i+1, len(strs)):
                    if strs[j] == None:
                        continue
                    else:
                        if sorted(strs[i]) == sorted(strs[j]):
                            this_group.append(strs[j])
                            strs[j] = None
                        else:
                            continue

                grouped_strs.append(this_group)
            return grouped_strs
