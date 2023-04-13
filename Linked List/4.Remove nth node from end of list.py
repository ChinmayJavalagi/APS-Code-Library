"""
1. Start the fast and slow pointers from the dummy node.
2. Move fast till n.
3. Then start moving slow and fast together till fast reaches None.
4. Attach slow.next to slow.next.next
"""

class Solution(object):
    def removeNthFromEnd(self, head, n):
        start = ListNode()
        start.next = head
        slow = fast = start
        for i in range(1,n+1):
            fast = fast.next
        
        while fast.next!=None:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return start.next
