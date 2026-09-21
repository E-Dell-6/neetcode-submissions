from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i = 0
        j = n - 1
        ans = 0
        
        while i < j:
            width = j - i
            curr = width * min(heights[i], heights[j])
            if curr > ans:
                ans = curr
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        
        return ans