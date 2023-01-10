class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for iterator in range(len(boxes)):
            array_sum = 0
            for iterator1 in range(len(boxes)):
                if boxes[iterator1] == '1':
                    array_sum += abs(iterator1 - iterator)
            answer.append(array_sum)
        return answer
                    
        