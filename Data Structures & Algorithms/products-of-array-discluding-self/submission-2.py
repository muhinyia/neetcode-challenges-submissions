class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [None]*len(nums)

   
        for i in range(len(nums)):
            product_before = 1
            product_after = 1
            for x in nums[:i]:
                product_before *= x
            for x in nums[i+1:]:
                product_after *= x 
            output[i] = (product_before * product_after)

        return output
        
        