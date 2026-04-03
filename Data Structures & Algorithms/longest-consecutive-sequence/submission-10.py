class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        numSet=set(nums)
        longest = 1
        for num in numSet:
            # if num-1 in numSet:
            #     continue
            # else:
                longestSub = 1
                while num+1 in numSet:
                    longestSub += 1
                    num+=1
                longest = max(longest, longestSub)
        return longest
