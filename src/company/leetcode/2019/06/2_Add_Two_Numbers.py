class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def fromList(self, list: []) -> ListNode:
        node = ListNode(list[0])
        if len(list) > 1:
            node.next = Solution.fromList(self, list[1:])
        return node

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        r = []
        ll1, ll2 = l1, l2
        while ll1 is not None or ll2 is not None:
            quotient = 0
            if ll1 is not None:
                quotient += ll1.val
                ll1 = ll1.next
            if ll2 is not None:
                quotient += ll2.val
                ll2 = ll2.next
            quotient += carry
            carry = int(quotient / 10)
            r.append(quotient % 10)
        if carry > 0:
            r.append(carry)
        return self.fromList(r)


s = Solution()
a = s.addTwoNumbers(s.fromList([2, 4, 3]), s.fromList([5, 6, 4]))
print(1)
