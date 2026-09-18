class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in numSet:
                thisLong = 1
                while num+1 in numSet:
                    thisLong += 1 
                    num += 1
                longest = max(longest, thisLong)
        return longest
        
