class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numSet = {}
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j]and i != j:
        #             return True
        # return False
        for num in nums:
            if num in numSet:
                return True
            else:
                numSet[num] = num
        return False