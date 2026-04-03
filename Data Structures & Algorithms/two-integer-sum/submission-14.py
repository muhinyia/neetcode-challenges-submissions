class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in hashMap.values():
                this_index = [k for k, v in hashMap.items() if v ==residual][0]
                return [this_index, i]
            else:
                hashMap[i] = nums[i]
        return []