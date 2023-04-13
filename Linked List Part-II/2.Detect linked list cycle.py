"""
Take two pointers fast and slow.
fast goes 2 step, slow goes one step.
if cycle exists they collide.
else fast will reach None
"""

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return 1
        return 0
