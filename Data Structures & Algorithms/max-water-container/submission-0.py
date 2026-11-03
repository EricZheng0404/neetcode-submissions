# brute force
class Solution:
    def maxArea(self, heights: List[int]) -> int:
        length = len(heights)
        result = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                vol = min(heights[i], heights[j]) * (j - i)
                if vol > result:
                    result = vol
        return result
            