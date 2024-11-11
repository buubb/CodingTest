from collections import defaultdict
class ListNode:
    def __init__(self, key:int, value:int):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:
    def __init__(self):
        self.size = 1000
        self.table = defaultdict(ListNode)

    def put(self, key:int, value:int) -> None:
        index = key % self.size # 모듈러 연산으로 해시테이블의 인덱스 구하기
        if self.table[index].value is None:
            self.table[index] = ListNode(key, value)
        p = self.table[index]
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None:
                break
            p = p.next
        return

    def get(self, key:int) -> int:
        index = key % self.size
        if self.table[index].value is None:
            return -1
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key:int) -> None:
        index = key % self.size
        if self.table[index].value is None:
            return
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next
