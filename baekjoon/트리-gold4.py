import sys
input = sys.stdin.readline

def find(k, parent):
    if parent[k] != k:
        parent[k] = find(parent[k], parent)
    return parent[k]

def union(a, b, parent, is_cycle):
    r1 = find(a, parent)
    r2 = find(b, parent)
    if r1 == r2:
         is_cycle[r1] = True
    if r1 < r2:
        parent[r2] = r1
        is_cycle[r1] |= is_cycle[r2]
    else:
        parent[r1] = r2
        is_cycle[r2] |= is_cycle[r1]

def solution():
    i = 1
    while True:
        n, m = map(int, input().split())
        if n==0 and m==0:
            break

        parent = list(range(n+1))
        is_cycle = [False] * (n+1)
        tree = set()
        for _ in range(m):
            v1, v2 = map(int, input().split())
            union(v1, v2, parent, is_cycle)
        
        
        for p in parent[1:]:
            r = find(p, parent)
            if not is_cycle[r]:
                 tree.add(r)
            
        cnt = len(tree)
        print(f"Case {i}: ", end='')
        if cnt <= 0:
            print("No trees.")
        elif cnt == 1:
                print("There is one tree.")
        else:
                print(f"A forest of {cnt} trees.")
        i+=1
            
solution()