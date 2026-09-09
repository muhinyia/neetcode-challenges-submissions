class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "????"
        encodedString = ""
        for i in range(len(strs)):

            encodedString += strs[i]
            if i <len(strs)-1:
                encodedString += "*#£SPLITHERE*#£"
        print(encodedString)
        return encodedString

    def decode(self, s: str) -> List[str]:
        if s =="????":
            return []
        strs = []
        for st in s.split("*#£SPLITHERE*#£"):
            strs.append(st)
        return strs
