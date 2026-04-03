# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         hashMap ={}
#         nums.sort()
#         for i in range(len(nums)):
#             start = i+1
#             end = len(nums)-1
#             while start<end:
#                 if nums[i] + nums[start] + nums[end] == 0:
#                     this_set = tuple(set([nums[i], nums[start], nums[end]]))
#                     if this_set in hashMap:
#                         pass
#                     else:
#                         hashMap[this_set] = [nums[i], nums[start], nums[end]]
#                     start += 1
#                     end -=1
#                 else:
#                     if nums[i] - (nums[start]+nums[end]) > 0:
#                         end -= 1
#                     else:
#                         start+=1

#         print(hashMap)
#         return list(hashMap.values())


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set() # Stores unique triplets as tuples
        
        for i, val1 in enumerate(nums):
            # Optimization: if the anchor is > 0, no sum can ever reach 0 again
            if val1 > 0:
                break
            # Skip duplicate anchors
            if i > 0 and val1 == nums[i-1]:
                continue
                
            seen = set() # Reset for each new anchor
            for j in range(i + 1, len(nums)):
                val2 = nums[j]
                complement = -val1 - val2
                
                if complement in seen:
                    # Found a triplet! Tuples are hashable and can go in 'res'
                    res.add((val1, complement, val2))
                
                seen.add(val2)
                
        return [list(triplet) for triplet in res]