class DataStream:

    def __init__(self, value: int, k: int):
        self.queue = deque()
        self.value = value
        self.k = k
        self.counter = 0
        

    def consec(self, num: int) -> bool:
        self.queue.append(num)
        if self.value == num:
            self.counter += 1
        if len(self.queue) > self.k and self.queue.popleft() == self.value:
                self.counter -= 1
        return self.counter == self.k
            


# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)