class Solution:
    def isPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1
        while start < end:
            if s[start].lower().isalnum() and s[end].lower().isalnum():
                if s[start].lower() != s[end].lower():
                    return False
                else:
                    start += 1
                    end -= 1
            else:
                if not s[start].lower().isalnum():
                    start += 1
                if not s[end].lower().isalnum():
                    end -= 1
        return True

