class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [None]*len(nums)
        preProd = 1
        posProd = 1
        for i in range(len(nums)):
            products[i] = preProd
            preProd *= nums[i]
        for i in range(len(nums)-1, -1, -1):
            products[i] *= posProd
            posProd *= nums[i]
        return products