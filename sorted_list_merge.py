from typing import Optional

# Merge the two lists into one sorted list. 
# The list should be made by splicing together 
# the nodes of the first two lists.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        # Iterate while both lists are not empty
        while list1 and list2:
            if list1.val < list2.val:
                # if list1 is smaller, append it to the merged list
                # and move to the next node in list1
                tail.next = list1
                list1 = list1.next
            else:
                # else, append list2 to the merged list
                # and move to the next node in list2
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next