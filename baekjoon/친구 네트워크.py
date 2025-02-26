import sys

input = sys.stdin.readline

class Solution:
    def find(self, k, parent):
        if parent[k] != k:
            parent[k] = self.find(parent[k], parent)  # 경로 압축 적용
        return parent[k]

    def union(self, a, b, parent, size):
        r1 = self.find(a, parent)
        r2 = self.find(b, parent)

        if r1 != r2:
            if size[r1] > size[r2]:  # 더 큰 쪽으로 합침
                parent[r2] = r1
                size[r1] += size[r2]
            else:
                parent[r1] = r2
                size[r2] += size[r1]

    def friends_network(self):
        T = int(input())
        for _ in range(T):
            n = int(input())
            person = {}
            parent = {}
            size = {}

            for _ in range(n):
                a, b = input().split()
                
                if a not in person:
                    person[a] = a
                    parent[a] = a
                    size[a] = 1
                if b not in person:
                    person[b] = b
                    parent[b] = b
                    size[b] = 1
                
                self.union(person[a], person[b], parent, size)
                
                root = self.find(person[a], parent)
                print(size[root])  # 루트의 크기 출력
                # print(parent) 원하는 값이 안나와서 ... 한번 더 find 처리를 해줘야할 듯듯듯듯

if __name__ == "__main__":
    s = Solution()
    s.friends_network()
