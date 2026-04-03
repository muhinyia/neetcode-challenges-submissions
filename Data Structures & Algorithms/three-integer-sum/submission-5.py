class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # d_d = {}
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for z in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[z] == 0:
        #                 this_set = tuple(sorted([nums[i], nums[j], nums[z]]))
        #                 print(this_set)
        #                 if this_set in d_d:
        #                     continue
        #                 else:
        #                     d_d[this_set] = [nums[i], nums[j], nums[z]]
        # return list(d_d.values())

        # Optimize by sorting
        nums.sort()
        triplets = {}
        for i in range(len(nums)):
            start = i+1
            end = len(nums)-1
            residual = 0-nums[i]
            while start<end:
                if nums[start] + nums[end] == residual:
                    if tuple([nums[i], nums[start], nums[end]]) in triplets:
                        pass
                    else:
                        triplets[tuple([nums[-1], nums[start], nums[end]])] = [nums[i], nums[start], nums[end]]
                    start += 1
                    end -= 1
                    continue
                else:
                    if nums[start] + nums[end] > residual:
                        end -= 1
                    else:
                        start += 1
        return list(triplets.values())

 

    