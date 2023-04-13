"""
1. Find the middle element using slow-fast approach.
2. Reverse the linked list from slow.next.
3. Start two pointers, one from beginning and another is slow pointer. check if the vals of both are equal.
"""

# TC - O(N/2)+O(N/2)+O(N/2)

def reverse(ptr):
    pre = None
    nex = None
    while ptr != None:
        nex = ptr.next
        ptr.next = pre
        pre = ptr
        ptr = nex
    return pre

def isPalindrome(head):
    if head == None or head.next == None:
        return True
    slow = head
    fast = head
    while fast.next != None and fast.next.next != None:
        slow = slow.next
        fast = fast.next.next
    slow.next = reverse(slow.next)
    slow = slow.next
    dummy = head
    while slow != None:
        if dummy.val != slow.val:
            return False
        dummy = dummy.next
        slow = slow.next
    return True
