class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        ans = 0
        i, j = 1, len(height) - 1
        lmax, rmax = height[0], height[-1]

        while i <= j:
            
            if height[i] > lmax:
                lmax = height[i]
            if height[j] > rmax:
                rmax = height[j]

            
            if lmax <= rmax:
                ans += lmax - height[i]
                i += 1
            
            else:
                ans += rmax - height[j]
                j -= 1

        return ans
        
