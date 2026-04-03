class Solution:
    def maxArea(self, heights: List[int]) -> int:
         
        # max_area = 0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         if heights[j]>=heights[i]:
        #             height = heights[i]
        #         else:
        #             height = heights[j]
        #         this_area  = height * (j-i)
        #         if this_area > max_area:
        #             max_area = this_area

        # return max_area

        start = 0
        end = len(heights) - 1
        max_area = 0
        while start<end:
            this_width = (end - start)
            min_height = min(heights[start], heights[end])
            this_area = this_width * min_height
            max_area = max(max_area, this_area)
            if heights[start] > heights[end]:
                # start +=1
                end -= 1
            else:
                # end -= 1
                start += 1
        return max_area




