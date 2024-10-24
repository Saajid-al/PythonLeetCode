# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):

        dummy = ListNode()
        tail = dummy
        while(list1 and list2):
            if(list1.val > list2.val):
                tail.next = list1.val
                list1 = list1.next
            else:
                tail.next = list2.val
                list2 = list2.next
            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2 
            
        return dummy.next

s = Solution()
print(s.mergeTwoLists([1,2,4], [1,3,4]))