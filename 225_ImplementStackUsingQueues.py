class MyStack:

    def __init__(self):
        self.q1 = deque()
        self.q2 = deque()

    def push(self, x: int) -> None:
        self._top = x
        self.q1.append(x)

    def pop(self) -> int:
        if len(self.q1) > 0:
            while len(self.q1) > 1:
                last_popped = self.q1.popleft()
                self.q2.append(last_popped)
                self._top = last_popped
            return self.q1.popleft()
        while len(self.q2) > 1:
            last_popped = self.q2.popleft()
            self.q1.append(last_popped)
            self._top = last_popped
        return self.q2.popleft() 

    def top(self) -> int:
        return self._top

    def empty(self) -> bool:
        return len(self.q1) + len(self.q2) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
