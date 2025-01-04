from collections import Counter

class Solution:
    def task_scheduler(self, tasks:list, n:int):
        cntr = Counter(tasks)
        result = 0
        while True:
            sub_count = 0
            for task,_ in cntr.most_common(n+1):
                sub_count += 1
                result += 1

                # 태스크 수를 하나 줄임
                cntr.subtract(task)
                # 빈 카운터를 더해 0 이하인 아이템을 목록에서 아예 제거
                cntr += Counter()
            
            if not cntr:
                break
        
            result += n - sub_count + 1

        print(result)



if __name__ == "__main__":
    s = Solution()
    tasks = ["A", "A", "A", "B", "B", "B"]
    s.task_scheduler(tasks, 2)
