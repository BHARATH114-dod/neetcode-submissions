class Solution:
    def trap(self, heights: List[int]) -> int:
        if not heights:
            return 0

        l, r = 0, len(heights) - 1
        leftmax, rightmax = heights[l], heights[r]
        res = 0

        while l < r:
            if leftmax < rightmax:
                l += 1
                leftmax = max(leftmax, heights[l])
                res += leftmax - heights[l]
            else:
                r -= 1
                rightmax = max(rightmax, heights[r])
                res += rightmax - heights[r]

        return res