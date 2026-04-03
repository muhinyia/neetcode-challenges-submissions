class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d_d = defaultdict(int)
        for num in nums:
            d_d[num]+=1
        top_k = []
        top_k = sorted(d_d.values())[::-1][:k]
        top_k_keys = []
        for key in d_d:
            if d_d[key] in top_k:
                top_k_keys.append(key)
            else:
                continue
        if top_k_keys != []: 
            return top_k_keys
        else:
            return nums