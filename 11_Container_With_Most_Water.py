class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
    
        res = 0
        while l < r:
            #finding distance
            dist = r - l
            #finding min tank to find area
            m = min(height[l] , height[r])
            area = dist * m
            if area > res:
                res = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
