from ListNode import *


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        refs = list()
        next_ = head
        length = 0
        while next_ is not None:
            refs.append(next_)
            next_ = next_.next
            length += 1

        idx = length - n
        if idx == 0:
            return head.next
        else:
            refs[idx - 1].next = refs[idx].next

        return head


l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(3)
l1.next.next.next = ListNode(4)
l1.next.next.next.next = ListNode(5)
exp = ListNode(1)
exp.next = ListNode(2)
exp.next.next = ListNode(3)
exp.next.next.next = ListNode(5)
s = Solution()
assert s.removeNthFromEnd(l1, 2) == exp