# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        a = []
        b = []
        L = []
        c = 0

        while l1:
            a.append(l1.val)
            l1 = l1.next

        while l2:
            b.append(l2.val)
            l2 = l2.next

        for i in range(max(len(a), len(b))):
            x = a[i] if i < len(a) else 0
            y = b[i] if i < len(b) else 0

            total = x + y + c

            L.append(total % 10)
            c = total // 10

        if c:
            L.append(c)
        dummy = ListNode(0)
        current = dummy

        for value in L:
            current.next = ListNode(value)
            current = current.next

        return dummy.next



        