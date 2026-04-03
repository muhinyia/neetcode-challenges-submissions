class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs==[""]: return " " 
        if strs==[]: return ""
        return "\t".join(s for s in strs)

    def decode(self, s: str) -> List[str]:
        if s == " ": return [""]
        if len(s)==0: return []
        return s.split("\t")
