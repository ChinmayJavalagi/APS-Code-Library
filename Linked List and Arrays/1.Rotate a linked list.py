"""
1. Iterate through the linked list, find the length of it and attach the next pointer of last node to first node to make it circular.
2. Suppose k is greater than length of the linked list then k%length.
3. Now we should remove the link of the kth node from end, so start traversing till length-k.
4. Assign the head to cur.next, and remove the link 
5. Return the head
"""

#TC - O(length)+O(length - (length%k))

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None or head.next == None or k == 0:
            return head
        cur = head
        length = 1
        while cur.next!=None:
            cur = cur.next
            length+=1
        cur.next = head

        k = k%length
        end = length-k
        while end:
            cur = cur.next
            end-=1
        head = cur.next
        cur.next = None
        return head
