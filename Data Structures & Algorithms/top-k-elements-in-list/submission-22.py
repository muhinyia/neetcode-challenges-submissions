class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1

        numsCounts = []
        for key, value in hashMap.items():
            numsCounts.append([value, key])
        
        numsCounts.sort(reverse=True)
        topK = []
        print(numsCounts)
        for i in range(k):
            topK.append(numsCounts[i][1])
        return topK
