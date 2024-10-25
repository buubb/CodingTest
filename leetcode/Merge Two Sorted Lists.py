class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLinkedLists(self, L1: ListNode, L2: ListNode) -> ListNode:
        if (not L1) or (L2 and L1.val > L2.val):
            L1 , L2 = L2, L1
        if L1:
            L1.next = self.mergeTwoLinkedLists(L1.next, L2)
        return L1

def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

L1 = [1,2,4]
L2 = [1,3,4]
A = create_linked_list(L1)
B= create_linked_list(L2)
solution = Solution()
print(solution.mergeTwoLinkedLists(A, B))