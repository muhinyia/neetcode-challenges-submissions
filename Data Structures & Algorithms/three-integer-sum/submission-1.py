class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        d_d = {}
        triplets = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for z in range(j+1, len(nums)):
                    if nums[i] + nums[j] + nums[z] == 0:
                        this_set = tuple(sorted([nums[i], nums[j], nums[z]]))
                        print(this_set)
                        if this_set in d_d:
                            continue
                        else:
                            d_d[this_set] = [nums[i], nums[j], nums[z]]
                            triplets.append([nums[i], nums[j], nums[z]])
        return triplets