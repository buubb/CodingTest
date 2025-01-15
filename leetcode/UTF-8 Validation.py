class Solution:
    def validUtf8(self):
        data = list(map(int, input().split()))
        # UTF-8에서는 첫 바이트를 제외한 나머지 바이트는 10xxxxxx로 구성되어야 함
        def check(size):
            for i in range(start + 1, start + size + 1):
                if i >= len(data) or (data[i] >> 6) != 0b10:
                    return False
            return True
        
        start = 0
        while start < len(data):
            first = data[start]

            if (first >> 3) == 0b11110 and check(3):
                start += 4
            elif (first >> 4) == 0b1110 and check(2):
                start += 3
            elif (first >> 5) == 0b110 and check(1):
                start += 2
            elif (first >> 7) == 0:
                start += 1
            else:
                return False
        return True

if __name__ == "__main__":
    s = Solution()
    s.validUtf8() 