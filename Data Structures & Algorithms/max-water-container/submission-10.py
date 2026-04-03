class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         if heights[i] >= heights[j]:
        #             height = heights[j]
        #         else:
        #             height = heights[i]
        #         this_area = height * (j-i)
        #         max_area = max(max_area, this_area)
        # return max_area

        start = 0
        end = len(heights)-1
        max_area = 0
        while start<end:
            width = end - start
            height = min(heights[start], heights[end])
            max_area = max((width*height), max_area)
            if heights[start] < heights[end]:
                start += 1
            else:
                end -= 1

        return max_area




        