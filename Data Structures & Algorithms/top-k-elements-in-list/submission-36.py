import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        pq = []
        for key, val in frequencies.items():
            heapq.heappush(pq, [val, key])

            if len(pq)>k:
                heapq.heappop(pq)

        topK = []

        for i in range(k):
            topK.append(pq[i][-1])

        return topK