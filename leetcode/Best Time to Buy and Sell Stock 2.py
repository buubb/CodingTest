
class Solution:
    # greedy
    def maxProfit(self, price:list):
        prev = price[0]
        total = 0
        for i in range(1, len(price)):
            if price[i] >= prev:
                total += price[i] - prev
            prev = price[i]
        print(total)
    
    #python
    def maxProfit2(self, price:list):
        print(sum(max(price[i+1] - price[i], 0) for i in range(len(price)-1)))


if __name__ == "__main__":
    s = Solution()
    arr = [7,1,5,3,6,4]
    s.maxProfit2(arr)