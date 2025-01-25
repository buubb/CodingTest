import sys
from collections import Counter
input = sys.stdin.readline

class Solution:
    # bruteforce : 시간초과
    def minimum_substring(self):
        S = input()
        T = input()
        def contains(s_substr_list, t_lst):
            for t_elem in t_lst:
                if t_elem in s_substr_list:
                    s_substr_list.remove(t_elem)
                else:
                    return False
            return True
        
        if not S or not T:
            return
        window_size = len(T)
        for size in range(window_size, len(S)+1):
            for left in range(len(S)-size+1):
                s_substr = S[left:left+size]
                if contains(list(s_substr), list(T)):
                    print(s_substr)
                    return
    
    def minimum_substring2(self):
        s = input()
        T = input()
        need = Counter(T)
        missing = len(T)
        left = start = end = 0

        # 오른쪽 포인터 이동
        for right, char in enumerate(s, 1):
            missing -= need[char]>0
            need[char] -= 1

            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right - left <= end-start:
                    start, end = left, right 

                need[s[left]] += 1
                missing += 1
                left += 1
        print(start, end)
        print(s[start:end])

    def minimum_substring3(self):
        s = input()
        t = input()
        t_count = Counter(t)
        current_count = Counter()

        start = float('-inf')
        end = float('inf')

        left = 0
        for right, char in enumerate(s,1):
            current_count[char] += 1

            while current_count & t_count == t_count:
                if right-left < end-start:
                    start, end = left, right
                current_count[s[left]] -= 1
                left += 1

        print(s[start:end] if end - start <= len(s) else '')


if __name__ == "__main__":
    s = Solution()
    s.minimum_substring3()