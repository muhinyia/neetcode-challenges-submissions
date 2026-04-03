from collections import OrderedDict
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

        for key, value in hashMap.items():
            numsCounts.append([value, key])

        numsCounts.sort()
        print(numsCounts)
        for i in range(k):
            kItems.append(numsCounts.pop()[1])
            

        return kItems

                
