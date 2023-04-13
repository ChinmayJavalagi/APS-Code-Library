"""
1. Using slow-fast approach reach a node where they collide.
2. Reassign the slow to the head and start moving slow and fast together till they meet again, this is the starting point of the loop.
"""

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = entry = head
        while fast!= None and fast.next!=None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != entry:
                    slow = slow.next
                    entry = entry.next
                return slow
        
        return None
