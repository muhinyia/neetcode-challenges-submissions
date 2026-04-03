class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in hashMap:
                return [hashMap[residual], i]
            else:
                hashMap[nums[i]] = i
        return []
        