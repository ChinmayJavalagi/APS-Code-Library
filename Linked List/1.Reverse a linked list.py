"""
1. Initialise prev --> None at first.
2. Start traversing, store the cur.next in a variable
3. Assign cur.next pointer to prev
4. move prev to the next node.
5. move cur to the next node using the variable that has stored cur.next
"""

#TC - O(n)
class Solution(object):
    def reverseList(self, head):
        cur = head
        prev = None
        while cur !=None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        return prev
