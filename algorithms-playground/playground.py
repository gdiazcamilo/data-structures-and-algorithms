from collections import deque


class MyQueue:

    def __init__(self):
        self.push_stack = deque()
        self.pop_stack = deque()

    def push(self, x: int) -> None:
        self.push_stack.append(x)

    def pop(self) -> int:
        if self.pop_stack:
            return self.pop_stack.pop()
        
        while self.push_stack:
            # reverse the order of items by poping from the `push_stack` and pushing to the `pop_stack`
            last_in_line = self.push_stack.pop()
            self.pop_stack.append(last_in_line)
        
        if self.pop_stack:
            return self.pop_stack.pop()
            

    def peek(self) -> int:
        if self.pop_stack:
            return self.pop_stack[-1]
        else:
            return self.push_stack[0]
        

    def empty(self) -> bool:
        return not self.push_stack and not self.pop_stack


d = MyQueue()
d.push(1)
d.push(2)
d.push(3)
print(d.peek())     # 1
print(d.pop())      # 1
print(d.peek())     # 2
print(d.pop())      # 2
print(d.peek())     # 3
print(d.empty())    # false
print(d.pop())      # 3
print(d.empty())    # true
