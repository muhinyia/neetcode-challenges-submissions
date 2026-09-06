class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashSet = {}
        for i in range(len(nums)):
            if (target - nums[i]) in hashSet:
                return [hashSet[(target - nums[i])], i]
            else:
                if nums[i] not in hashSet:
                    hashSet[nums[i]] = i
                else:
                    continue

        return 