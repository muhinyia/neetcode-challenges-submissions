class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in nums[i+1:]:
                return [i, nums.index(residual, i+1, len(nums))]
            
        