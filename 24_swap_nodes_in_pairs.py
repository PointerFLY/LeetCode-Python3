from ListNode import *


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        k = 2
        refs = list()
        next_ = head
        is_first_box = True
        previous_box_last = None

        while next_ is not None:
            refs.append(next_)

            if len(refs) == k:
                if is_first_box:
                    head = refs[-1]
                    is_first_box = False

                next_box_head = next_.next
                for i in range(k - 1, 0, -1):
                    refs[i].next = refs[i - 1]
                refs[0].next = next_box_head

                if previous_box_last:
                    previous_box_last.next = refs[-1]
                previous_box_last = refs[0]

                next_ = refs[0]
                refs = list()

            next_ = next_.next

        return head


l = ListNode(1)
l.next = ListNode(2)
l.next.next = ListNode(3)
l.next.next.next = ListNode(4)
l.next.next.next.next = ListNode(5)
exp = ListNode(2)
exp.next = ListNode(1)
exp.next.next = ListNode(4)
exp.next.next.next = ListNode(3)
exp.next.next.next.next = ListNode(5)
s = Solution()
assert s.reverseKGroup(l, 2) == exp