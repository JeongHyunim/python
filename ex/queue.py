import sys
queue = []
x = int(input())
for i in range(x):
    lst = list(sys.stdin.readline().split())
    if lst[0] == 'push':
        queue.append(lst[-1])
    elif lst[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            del queue[0]
    elif lst[0] == 'size':
        print(len(queue))
    elif lst[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif lst[0] == 'front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    elif lst[0] == 'back':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])

print(queue)