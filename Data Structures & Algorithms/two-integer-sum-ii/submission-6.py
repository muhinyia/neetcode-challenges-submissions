class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # for i in range(0, len(numbers)):
        #     for j in range(i+1, len(numbers)):
        #         if numbers[i] + numbers[j] == target:
        #             return[i+1, j+1]

        # return []


        start = 0
        end = len(numbers)-1
        while start<end:
            if numbers[start] + numbers[end] > target:
                end -= 1
                continue
            if numbers[start] + numbers[end]<target:
                start += 1
                continue
            else:
                return [start+1, end+1]
        return []

