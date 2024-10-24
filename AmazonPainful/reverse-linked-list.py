# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        curr = head 
        prev = None

        while curr: #while we have anode
            nxt = curr.next #our pointer to our next node
            curr.next = prev #change our next pointer to equal to the previous
            prev = curr #change the previous to the now new current poiinter
            curr = nxt #change the current pointer to the actual next pointer
        return prev
