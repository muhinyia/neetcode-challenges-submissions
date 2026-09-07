class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1
        buckets = {}
        for num, freq in frequencies.items():
            if freq in buckets:
                buckets[freq].append(num)
            else:
                buckets[freq] = [num]
        
        topK = sorted(buckets.keys())[::-1][:k]

        print(buckets)
        print(topK)

        results = []
        for i in topK:
            for item in buckets[i]:
                if len(results) == k:
                    continue
                else:
                    results.append(item)

        print(results)

        return results