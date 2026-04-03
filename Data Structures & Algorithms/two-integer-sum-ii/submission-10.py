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
            if numbers[start] + numbers[end] == target:
                return [start+1, end+1]
            else:
                if numbers[start] + numbers[end] > target:
                    end -= 1
                else:
                    start += 1
        return []

