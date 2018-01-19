from ListNode import *


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        node = head
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                node.next = l1
                l1 = l1.next
            else:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1 is not None:
            node.next = l1
        else:
            node.next = l2

        return head.next


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)
l2 = ListNode(0)
l2.next = ListNode(0)
l2.next.next = ListNode(4)
ret = ListNode(0)
ret.next = ListNode(0)
ret.next.next = ListNode(1)
ret.next.next.next = ListNode(2)
ret.next.next.next.next = ListNode(4)
ret.next.next.next.next.next = ListNode(4)
s = Solution()
print(s.mergeTwoLists(l1, l2), ret)
assert s.mergeTwoLists(l1, l2) == ret
