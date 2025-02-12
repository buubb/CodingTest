def thinking_heap(n, k, p):
    # 힙 배열 초기화 (1-based index 사용)
    heap = [None] * (n + 1)
    insert_order = []

    # Step 1: p 위치에 k 배치
    heap[p] = k
    insert_order.append(k)

    # Step 2: 조상 노드 채우기
    current_value = k - 1
    parent = p // 2
    while parent > 0:
        if current_value <= 0:
            print(-1)
            return
        heap[parent] = current_value
        insert_order.append(current_value)
        current_value -= 1
        parent //= 2

    # Step 3: 자식 노드 채우기
    current_value = k + 1

    def fill_subtree(node):
        nonlocal current_value
        if node > n:
            return
        if heap[node] is None:
            if current_value > n:
                print(-1)
                return
            heap[node] = current_value
            insert_order.append(current_value)
            current_value += 1
        fill_subtree(2 * node)
        fill_subtree(2 * node + 1)

    fill_subtree(p * 2)
    fill_subtree(p * 2 + 1)

    # Step 4: 나머지 노드 채우기
    for i in range(1, n + 1):
        if heap[i] is None:
            while current_value in insert_order:
                current_value += 1
            if current_value > n:
                print(-1)
                return
            heap[i] = current_value
            insert_order.append(current_value)

    # 삽입 순서 출력
    for value in insert_order:
        print(value)

# 입력 예시
n = int(input())
k, p = map(int, input().split())
thinking_heap(n, k, p)
