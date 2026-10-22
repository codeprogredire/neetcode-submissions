class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        n = len(heights)

        l = 0
        r = n-1

        while l < r:
            area = (r-l) * min(heights[l],heights[r])
            ans = max(ans,area)

            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1
        return ans
        