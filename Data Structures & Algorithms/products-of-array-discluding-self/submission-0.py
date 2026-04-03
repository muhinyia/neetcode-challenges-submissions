class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = []
        for i in range(len(nums)):
            this_product = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                this_product *= nums[j]
            products.append(this_product)
        return products
            