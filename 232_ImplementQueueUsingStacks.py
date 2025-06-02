"""
This was a really fun problem. I broke the problem down on pen and paper
before implementing it, which was extremely satisfying. I also had an important
lesson about not mutating objects as I iterate over them, when I attempted to 
get clever and use list comprehension instead of while loops in pop() and peek(0).
"""
class MyQueue:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, x: int) -> None:
        self.s1.append(x)

    def pop(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        res = self.s2.pop()
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res
        
    def peek(self) -> int:
        while len(self.s1) > 0:
            self.s2.append(self.s1.pop())
        res = self.s2[-1]
        while len(self.s2) > 0:
            self.s1.append(self.s2.pop())
        return res

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
