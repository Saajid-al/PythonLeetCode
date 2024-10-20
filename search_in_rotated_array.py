class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        

        l = 0
        r = 0
        res = nums[0]
        while(l <= r):
            m = (l+r)//2 
            if target==nums[m]:
                return m
            if(nums[l] > target < nums[m]):
                l = m + 1 
            elif

          


s = Solution()
print(s.search([4,5,6,7,0,1,2], 0))