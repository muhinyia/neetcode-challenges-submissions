class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[i] >= heights[j]:
                    height = heights[j]
                else:
                    height = heights[i]
                this_area = height * (j-i)
                max_area = max(max_area, this_area)
        return max_area