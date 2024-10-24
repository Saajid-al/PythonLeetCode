class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        
        hashset = set(nums1)
        lst = []
        for num in nums2:
            if num in hashset and num not in lst:
                lst.append(num)
        return lst

s = Solution()
print(s.intersection([1,2,2,1], [2,2]))