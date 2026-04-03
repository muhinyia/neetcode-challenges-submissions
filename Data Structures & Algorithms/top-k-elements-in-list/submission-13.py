class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # nums_set = {}

        # for num in nums:
        #     if num in nums_set:
        #         nums_set[num] += 1
        #     else:
        #         nums_set[num] = 1
        
        # nums_set_elements = []
        # for num, val in nums_set.items():
        #     nums_set_elements.append([val, num])

        # nums_set_elements.sort()
        # top_k_most_elements = []
        # for items in nums_set_elements[::-1][:k]:
        #     top_k_most_elements.append(items[-1])     

        # return top_k_most_elements 
        num_set = {}
        for num in nums:
            if num in num_set:
                num_set[num] += 1
            else:
                num_set[num] = 1
        heap = []
        for key, value in num_set.items():
            heapq.heappush(heap,(value, key))
            if len(heap) > k:
                heapq.heappop(heap)

        top_k_elements = []
        i = 0

        while i<k:
            top_k_elements.append(heapq.heappop(heap)[1])
            i+=1
        return top_k_elements
    
        