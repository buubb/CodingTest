import sys
input = sys.stdin.readline

class Solution:
    def search_doc(self):
        words = input().strip()
        search = input().strip()
        cnt = 0
        i=0
        while i < len(words):
            if words[i:i+len(search)] == search:
                i += len(search)
                cnt += 1
            else:
                i+=1
        print(cnt)
            


if __name__ == "__main__":
    s = Solution()
    s.search_doc()