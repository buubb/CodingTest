import sys
input = sys.stdin.readline

def find(k, parent):
    if parent[k] != k :
        parent[k] = find(parent[k], parent)
    return parent[k]

def union(a, b, parent):
    r1 = find(a, parent)
    r2 = find(b, parent)

    if r1 < r2:
        parent[r2] = r1
    else:
        parent[r1] = r2
    
def solution():
    n, m = map(int, input().split())
    parent = list(range(n))
    games = []
    for _ in range(m):
        games.append(list(map(int, input().split())))
    cnt = 0
    for a, b in games:
        cnt += 1
        if find(a, parent) == find(b, parent):
            break
        else:
            union(a, b, parent)
    else:
        print(0)
        return
    print(cnt)


solution()