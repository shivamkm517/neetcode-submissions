class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_w = float('-inf')

        left = 0
        right = len(heights) - 1
        curr_water = 0
        while left < right:
            curr_water = min(heights[left], heights[right]) * (right - left)
            max_w = max(max_w, curr_water)

            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1

        return max_w

