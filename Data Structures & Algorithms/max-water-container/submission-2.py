class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # start = 0
        # end = len(heights)-1
        # max_height = heights[start]
        # max_width = len(heights)-1
        # currentArea = max_height * max_width

        # while start < end:
        #     if heights[start] * 
        max_area = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                if heights[j]>=heights[i]:
                    height = heights[i]
                else:
                    height = heights[j]
                this_area  = height * (j-i)
                if this_area > max_area:
                    max_area = this_area

        return max_area




