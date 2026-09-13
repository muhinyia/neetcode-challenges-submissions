class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]* len(nums)
        thisProduct = 1
        for i in range(len(nums)):
            products[i] = thisProduct
            thisProduct = products[i] * nums[i]

        thisProduct = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] = products[i] * thisProduct
            thisProduct *= nums[i] 
        return products