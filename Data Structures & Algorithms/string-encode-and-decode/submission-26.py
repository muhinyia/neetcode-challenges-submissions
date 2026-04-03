class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs: return ""
        if strs ==  [""]: return " "
        return "\t%".join(s for s in strs)

    def decode(self, str:str) -> List[str]:
        if not str: return []
        if str==" ": return [""]
        return str.split("\t%")

    