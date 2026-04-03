class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [None]*len(nums)
        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i ==j:
                    print(f"skipping {i}")
                else:
                    product *= nums[j]
            products[i] = product

        return products