import sys
from collections import deque
input = sys.stdin.readline

class Solution:
    def upstairs(self):
        N = int(input())
        scores = [int(input()) for _ in range(N)]
        
        def bfs():
            if N == 1:
                return scores[0]
            if N == 2:
                return scores[0] + scores[1]
            
            # 큐 초기화 및 방문 상태 관리
            Q = deque()
            visited = {}  # 방문 상태를 (i, count)로 기록하고 점수만 저장
            max_score = 0
            
            # 초기 상태 추가
            Q.append((0, scores[0], 1))  # (현재 인덱스, 누적 점수, 연속 이동 횟수)
            visited[(0, 1)] = scores[0]
            Q.append((1, scores[1], 1))  # 첫 계단을 건너뛴 경우
            visited[(1, 1)] = scores[1]
            
            while Q:
                i, score, count = Q.popleft()
                
                # 마지막 계단에 도달한 경우 최대 점수 갱신
                if i == N - 1:
                    max_score = max(max_score, score)
                    continue
                
                # 다음 상태 계산
                # 1칸 이동
                if i + 1 < N and count < 2:
                    next_state = (i + 1, count + 1)
                    next_score = score + scores[i + 1]
                    if next_state not in visited or visited[next_state] < next_score:
                        Q.append((i + 1, next_score, count + 1))
                        visited[next_state] = next_score
                
                # 2칸 이동
                if i + 2 < N:
                    next_state = (i + 2, 1)
                    next_score = score + scores[i + 2]
                    if next_state not in visited or visited[next_state] < next_score:
                        Q.append((i + 2, next_score, 1))
                        visited[next_state] = next_score
            
            return max_score
        
        print(bfs())

if __name__ == "__main__":
    s = Solution()
    s.upstairs()
