# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        self_next = self
        other_next = other
        while self_next is not None and other_next is not None:
            if self_next.val != other_next.val:
                return False
            self_next = self_next.next
            other_next = other_next.next

        if (self_next is not None and other_next is None) \
                or (self_next is None and other_next is not None):
            return False

        return True


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_node = l1
        l2_node = l2

        sum_node = None
        head = None
        carry = 0

        while l1_node is not None or l2_node is not None or carry != 0:
            sum_ = carry
            if l1_node is not None:
                sum_ += l1_node.val
                l1_node = l1_node.next
            if l2_node is not None:
                sum_ += l2_node.val
                l2_node = l2_node.next

            carry = int(sum_ / 10)
            sum_ = sum_ % 10

            if head is None:
                sum_node = ListNode(sum_)
                head = sum_node
            else:
                sum_node.next = ListNode(sum_)
                sum_node = sum_node.next

        return head


l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)
l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
expect = ListNode(7)
expect.next = ListNode(0)
expect.next.next = ListNode(8)
s = Solution()
answer = s.addTwoNumbers(l1, l2)
assert answer == expect
