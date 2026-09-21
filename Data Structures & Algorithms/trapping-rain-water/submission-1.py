class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        ans = 0
        i = 0

        while i < n - 1:
            while i < n and height[i] == 0:
                i += 1
            if i >= n - 1:
                break

            left = height[i]
            j = i + 1
            peak = j
            while j < n and height[j] < left:
                if height[j] > height[peak]:
                    peak = j
                j += 1

            if j < n:
                end = j
            else:
                end = peak

            wall = min(left, height[end])
            for k in range(i + 1, end):
                ans += wall - height[k]
            i = end

        return ans