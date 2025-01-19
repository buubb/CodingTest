import sys, string
input = sys.stdin.readline

class Solution:
    def decrypt(self):
        encrypt = input().strip()
        n = int(input())
        dictionary = [input().strip() for _ in range(n)]
        alphabets = [i for i in string.ascii_lowercase]
        
        printed = False
        # 암호문을 해독할 필요가 없는 경우
        for word in dictionary:
            if word in encrypt:
                print(encrypt)
                printed = True
                break
        
        if not printed:
            for i in range(1,26):
                alpha = {}
                for j in range(26):
                    a = j+i
                    if a > 25:
                        a -= 26
                    alpha[alphabets[j]] = alphabets[a]
                decode = ""
                for j in encrypt:
                    decode += alpha[j]
                for j in dictionary:
                    if j in decode:
                        print(decode)
                        break



    
        
        

                    
        

if __name__ == "__main__":
    s = Solution()
    s.decrypt()
        