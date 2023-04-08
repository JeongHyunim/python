import sys
stack = []
x= int(input())
print(x)
for i in range(x):
    lst = list(sys.stdin.readline().split())
    if lst[0] == 'push':
        stack.append(lst[1])
    if lst[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            del stack[-1]
    if lst[0] == 'size':
        print(len(stack))
    if lst[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if lst[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])