class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        
        maxFreqs = sorted(frequencies.values())[::-1][:k]
        topK = [None]*k
        # for key in frequencies:
        #     for i in range(k):
        #         if maxFreqs[i] == frequencies[key]:
        #             topK[i]=key
        #         else:
        #             pass

        for i in range(k):
            for key in frequencies:
                if maxFreqs[i] == frequencies[key] and key not in topK:
                    topK[i] = key
                else:
                    pass
        return topK