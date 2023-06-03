class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i in range(len(tasks)):
           tasks[i].append(i)
        tasks.sort(key=lambda x:(x[0],x[1],x[2]))

        result  = []
        queue = []

        t = 1
        for task in tasks:
            while t < task[0] and len(queue)>0:
                dur,i,start = heapq.heappop(queue)
                result.append(i)
                if start > t:
                    t = start
                t += dur


            heapq.heappush(queue, (task[1],task[2],task[0]))

        while len(queue)>0:
                dur,i,start = heapq.heappop(queue)
                result.append(i)

        return result