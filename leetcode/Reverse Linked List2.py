class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

class Solution:
    def reverseBetween(self, head:ListNode, m:int, n:int) -> ListNode:
        if not head or m==n:
            return head
        
        root = start = ListNode(None)
        root.next = head

        for _ in range(m-1):
            start = start.next
        end = start.next

        for _ in range(m,n):
            tmp , start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next


def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

arr = [1,2,3,4,5,6]
l1 = create_linked_list(arr)
m, n = map(int,input().split())
solution = Solution()
print(linked_list_to_list(solution.reverseBetween(l1,m,n)))