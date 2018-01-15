# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        res = ListNode(7)
        res.next = ListNode(0)
        res.next.next = ListNode(8)

        l_node = l1
        r_node = l2

        sum = None

        while l_node is not None or r_node is not None:
            if l_node is not None:
                pass
            if r_node is not None:
                pass


s = Solution()
l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
res = ListNode(7)
res.next = ListNode(0)
res.next.next = ListNode(8)
assert s.addTwoNumbers(l1, l2) == res
