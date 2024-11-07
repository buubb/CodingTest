import heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next=next

class Solution:
    def mergeKLists(self, lists:list[ListNode]) -> ListNode:
        root = result = ListNode(None)
        heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i, lists[i]))
        
        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            result.next = node[2]

            result = result.next
            if result.next:
                heapq.heappush(heap, (result.next.val, idx, result.next))

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

lists = []
a1 = [1,4,5]
a2 = [1,3,4]
a3 = [2,6]
solution = Solution()
lists.append(solution.create_linked_list(a1))
lists.append(solution.create_linked_list(a2))
lists.append(solution.create_linked_list(a3))
print(solution.linked_list_to_list(solution.mergeKLists(lists)))