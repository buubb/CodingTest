class ListNode:
    def __init__(self, val=0, next=None):
        self.next = next
        self.val = val

class Solution:
    def oddEvenList(self, head:ListNode) -> ListNode:
        if head is None:
            return None
        
        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            odd = odd.next
            even = even.next
        
        odd.next = even_head

        return head


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

arr = [1,2,3,4,5]
arr2 = [2,1,3,5,6,4,7]
l1 = create_linked_list(arr)
l2 = create_linked_list(arr2)

solution = Solution()
print(linked_list_to_list(solution.oddEvenList(l1)))
print(linked_list_to_list(solution.oddEvenList(l2)))





