n = int(input())
lst = []
for i in range(n):
    tri = list(map(int,input().split()))
    lst.append(tri)
ans = []
for i in range(n-1,-1,-1):
    temp = []
    for j in range(i,n):
        temp.append(lst[j][i])
    ans.append(temp)

for i in range(n):
    a = ans[i]
    print(a)
