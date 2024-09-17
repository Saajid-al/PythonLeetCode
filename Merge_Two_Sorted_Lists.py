class Solution(object):
    def mergeTwoLists(self, list1, list2):
        for x,s in enumerate(list1):
            print(list1[x], list2[x], end= " ")
            
s = Solution()
(s.mergeTwoLists([1,2,4], [1,3,4]))