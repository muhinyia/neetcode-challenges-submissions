class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_new = ""
        for char in s:
            if char.isalnum():
                s_new += char
        # print(s_new[::-1].split())
        return s_new.lower().split() == s_new[::-1].lower().split()