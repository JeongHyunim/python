N = 9
lst = []
answer = []

for i in range(N):
    x= int(input())
    lst.append(x)

summed = sum(lst)
lst = sorted(lst)

for i in range(len(lst)):
    for j in range(i + 1,len(lst)):
        if summed - lst[i]-lst[j]== 100:
            for k in range(9):
                if k != i and k !=j:
                    print(lst[k])