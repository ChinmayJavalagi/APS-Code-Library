"""
Fast moves two steps, slow move one step, by the time fast reaches end of the LL, slow will be at the middle.
"""

#TC - O(n)

class Solution(object):
    def middleNode(self, head):
        slow, fast = head, head
        while fast and fast.next and slow:
            fast = fast.next.next
            slow = slow.next
        return slow
