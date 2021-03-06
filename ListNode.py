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

    def __str__(self):
        self_next = self.next
        str_ = str(self.val)
        while self_next is not None:
            str_ += '->'
            str_ += str(self_next.val)
            self_next = self_next.next

        return str_
