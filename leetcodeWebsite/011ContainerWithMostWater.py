class Solution:
    def maxArea(self, height: List[int]) -> int:
        lh, rh = height[0], height[-1]
        i, j = 0, len(height) -1
        m = 0
        while i < j:
            m = max(m, min(lh, rh) * (j - i))
            if lh < rh:
                while i < j and height[i] <= lh:
                    i += 1
                lh = height[i]
            else:
                while i < j and height[j] <= rh:
                    j -= 1
                rh = height[j]
        return m