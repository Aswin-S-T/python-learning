# stack implementation in python

def create_stack():
    stack = []
    return stack

def push(stack,item):
    stack.append(item)
    return stack

def is_empty(stack):
    top = len(stack)
    if top == 0:
        top = -1
    return top == -1

def pop(stack,item):
    stack.pop(item)
    return stack


stack = create_stack()
print('Initial stack ---------', stack)
stack = push(stack,1)
push(stack,2)
push(stack,3)
push(stack,4)
print('Final stack--------', stack)