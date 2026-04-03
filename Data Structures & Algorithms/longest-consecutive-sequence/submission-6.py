class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        numSet = set(nums)
        longestSequence = 1
        for num in numSet:
            if num-1 in numSet:
                continue
            else:
                longestSubSequence = 1
                while num+1 in numSet:
                    longestSubSequence += 1
                    num += 1

            longestSequence = max(longestSequence, longestSubSequence)
        return longestSequence
        