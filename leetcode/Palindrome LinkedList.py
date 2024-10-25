class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head

        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        if fast:
            slow = slow.next
        
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        return not rev

# 일반 리스트를 ListNode 연결 리스트로 변환하는 함수
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

# 테스트 리스트
values = [1, 2, 2, 1]

# 리스트를 연결 리스트로 변환
head = create_linked_list(values)

# isPalindrome 메서드 호출
solution = Solution()
print(solution.isPalindrome(head))  # 출력: True
