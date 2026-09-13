class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        preProds, postProds =[0]*len(nums), [0]*len(nums)
        preProds[0] = postProds[len(nums)-1] = 1
        prods = [0] * len(nums)
        for i in range(1,len(nums)):
            preProds[i]= preProds[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            postProds[i] = postProds[i+1] * nums[i+1]
        for i in range(len(nums)):
            prods[i] = preProds[i] * postProds[i]
        return prods
        