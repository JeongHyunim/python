lst = []
for i in range(9):
    x = int(input())
    lst.append(x)
target = max(lst)
print(target)
print(lst.index(target))
