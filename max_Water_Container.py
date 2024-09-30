class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_area = 0
        while l < r:
            length = r - l
            maxHeight = min(height[l], height[r])
            max_area = max(max_area,maxHeight*length)
            if height[l] > height[r]:
                r -= 1 
            else:
                l += 1 
        return max_area

s = Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))
