# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        if not l2:
            return l1
        
        l1.val += l2.val
        if l1.val >= 10:
            l1.next = self.addTwoNumbers(ListNode(l1.val // 10), l1.next)
            l1.val %= 10       
        l1.next = self.addTwoNumbers(l1.next, l2.next)
        return l1

def main():
    test = Solution()
    result = test.addTwoNumbers(ListNode(2,ListNode(4,ListNode(3,None))),ListNode(5,ListNode(6,ListNode(4,None))))
    print(result.next.next.val,result.next.val,result.val)


if __name__ == '__main__':
    main()
