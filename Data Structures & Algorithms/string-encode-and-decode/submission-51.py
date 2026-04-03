class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return " "
        return "£££££".join([s for s in strs])

    def decode(self, s: str) -> List[str]:
        if s ==" ":
            return []
        return [st for st in s.split("£££££")]

