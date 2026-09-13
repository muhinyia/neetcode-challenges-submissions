class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1] * len(nums)
        preProduct = 1
        for i in range(len(nums)):
            products[i] = preProduct
            preProduct = products[i] * nums[i]

        postProduct = 1
        for i in range(len(nums)-1, -1, -1):
            products[i] = products[i] * postProduct
            postProduct *= nums[i] 
        return products