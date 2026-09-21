class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0
        for num in nums:
            if num-1 not in numSet:
                thisLongest = 1
                while num+1 in numSet:
                    thisLongest += 1
                    num+=1
                longest = max(longest, thisLongest)
        return longest