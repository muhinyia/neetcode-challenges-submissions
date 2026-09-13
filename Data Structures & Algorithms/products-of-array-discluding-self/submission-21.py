class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prods = [1]*len(nums)
        pre = post = 1
        for i in range(len(nums)):
            prods[i] = pre
            pre *= nums[i]

        for i in range(len(nums)-1, -1, -1):
            prods[i] *= post
            post *= nums[i]

        return prods