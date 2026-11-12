class Solution:
    def maxArea(self, heights: List[int]) -> int:

        l = maxRecord = 0
        r = len(heights)-1

        while l < r:

            width = r - l
            high = min(heights[l],heights[r])

            area = width*high

            if area > maxRecord:
                maxRecord = area
            
            if heights[l] < heights[r]:
                l += 1

            else:
                r -= 1
        
        return maxRecord