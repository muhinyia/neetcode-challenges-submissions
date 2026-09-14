class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append(",")
        res.append("#")
        res.extend(strs)
        print(res)
        return "".join(res)


    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, i, strs = [], 0, []
        print(s)
        while s[i] != "#":
            j = i
            while s[j] != ",":
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        print(sizes)
        for sz in sizes:
            j = i + int(sz)
            strs.append(s[i:j])
            i += int(sz) 
        return strs