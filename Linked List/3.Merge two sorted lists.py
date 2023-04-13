"""
Here we consider head of list1 as the node that should be returned.
1. We first check if list1.val>list2.val 
      if yes, we swap.
2. Assign head of list1 to a variable.
3. Iterate through the lists,
      if list1.val<list2.val, continue. also keep a temp for the previous node
      else, attach the temp.next to list2 and swap list1 and list2.
4. Return head of list1 stored in res
"""

#TC - O(n+m)

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        if list1 == None: return list2
        if list2 == None: return list1

        if list1.val >list2.val:
            list1,list2 = list2,list1
        res = list1

        while list1!=None and list2!=None:
            temp = None
            while list1!=None and list1.val<=list2.val:
                temp = list1
                list1 = list1.next
            temp.next = list2
            list1,list2 = list2,list1
        return res
