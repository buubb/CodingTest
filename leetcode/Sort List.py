class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2:ListNode) -> ListNode:
        if l1 and l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoLists(l1.next, l2)

        return l1 or l2
    
    def sortList(self, head:ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next

        half.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeTwoLists(l1,l2)

class Solution2:
    def sortList(self, head:ListNode) -> ListNode:
        # 연결리스트 -> 파이썬 리스트
        p = head
        lst: list = []
        while p:
            lst.append(p.val)
            p = p.next
        
        # 정렬
        lst.sort()

        # 파이썬 리스트 -> 연결리스트
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head
