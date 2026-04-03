class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProd = 1
        postProd = 1
        products = [None] * len(nums)
        for i in range(len(nums)):
            products[i] = preProd
            preProd *= nums[i]
        for j in range(len(nums)-1, -1, -1):
            products[j] *= postProd
            postProd *= nums[j]
        return products