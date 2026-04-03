class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Bruteforce
        if not s:
            return 0
        longest = 1
        for i in range(len(s)):
            this_longest = 1
            seen = []
            for j in range(i+1,len(s)):
                if s[i] != s[j] and s[j] not in seen:
                    this_longest += 1
                    seen.append(s[j])
                else:
                    break
            longest = max(longest, this_longest)

        return longest