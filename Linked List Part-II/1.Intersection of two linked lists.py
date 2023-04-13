"""
1. Take two dummy nodes for each list. Point each to the head of the lists.
2. Iterate over them. If anyone becomes null, point them to the head of the opposite lists 
and continue iterating until they collide.
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        cur1, cur2 = headA, headB
        while cur1 != cur2:
            cur1 = headB if cur1 == None else cur1.next
            cur2 = headA if cur2 == None else cur2.next
        return cur1
