class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxWater = 0
        n = len(heights)
        start = 0
        end = n-1
        while start < end:
            curr_x = end - start
            curr_y = min(heights[start],heights[end])
            curr_water = curr_x * curr_y
            if curr_water > maxWater:
                maxWater = curr_water
            if curr_y == heights[start]:
                start += 1
                continue
            if curr_y == heights[end]:
                end -= 1
                continue
        return maxWater
            
