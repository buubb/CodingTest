class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head:ListNode) -> ListNode:
        node, prev = head, None

        while node:
            node.next, next = prev, node.next
            prev, node = node, next

        return prev

class Solution2:
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        root = head = ListNode(0)

        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1
                l1 = l1.next
            if l2:
                sum += l2
                l2 = l2.next
            
            carry, val = divmod(sum + carry, 10)
            head.next = ListNode(val)
            head = head.next
        
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

def add_two_list(L1: ListNode , L2: ListNode) -> ListNode:
    a = linked_list_to_list(L1)
    b = linked_list_to_list(L2)

    a_join = ''.join(str(e) for e in a)
    b_join = ''.join(str(e) for e in b)
    c = int(a_join) + int(b_join)

    return create_linked_list(str(c))
    

solution = Solution()
arr1 = [2, 4, 3]
arr2 = [5, 6, 4]
reverse_linked_list1 = solution.reverseList(create_linked_list(arr1))
reverse_linked_list2 = solution.reverseList(create_linked_list(arr2))
result = solution.reverseList(add_two_list(reverse_linked_list1, reverse_linked_list2))

print(linked_list_to_list(result))