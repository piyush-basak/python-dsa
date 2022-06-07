from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('Initital stack:')
print(stack)

print(stack.pop())
print(stack.pop())
print(stack.pop())

print('stack after pop operation')
print(stack)
