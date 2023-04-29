import sys
deck = []
x = int(input())
for i in range(x):
    lst = list(sys.stdin.readline().split())
    if lst[0] == 'push_back':
        deck.append(lst[-1])
    elif lst[0] == 'push_front':
        deck.insert(0, lst[-1])
    elif lst[0] == 'pop_front':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck[0])
            del deck[0]
    elif lst[0] == 'pop_back':
        if len(deck) == 0:
            print(-1)
        else:
            print(deck.pop())
    elif lst[0] == 'size':
        print(len(deck))
    elif lst[0] == 'empty':
        if len(deck) == 0:
            print(1)
        else:
            print(0)
    elif lst[0] == 'front':
        if len(deck)==0:
            print(-1)
        else:
            print(deck[0])
    elif lst[0] == 'back':
        if len(deck)==0:
            print(-1)
        else:
            print(deck[-1])

print(deck)