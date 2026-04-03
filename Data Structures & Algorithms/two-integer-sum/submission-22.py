class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] == target and i != j:
        #             return [i, j]
        # return []
        hashMap = {}
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in hashMap:
                return [min(hashMap[residual], i), max(hashMap[residual], i)]
            else:
                hashMap[nums[i]] = i
        return []
