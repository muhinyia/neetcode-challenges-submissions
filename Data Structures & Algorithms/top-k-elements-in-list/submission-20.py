class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1   

        kItems = []
        numsCounts = [] 

        for num, count in hashMap.items():
            numsCounts.append([count, num])
            
        numsCounts.sort() # sorts sublists based on counts -> 

        for i in range(k):
            kItems.append(numsCounts.pop()[1])

        return kItems

                
