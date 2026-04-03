class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_set = []
        for num in nums:
            if num in nums_set:
                return True
            nums_set.append(num)
        return False
        # return not len(set(nums)) == len(nums)
        