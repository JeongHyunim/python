n,m = map(int,input().split(' '))
x = []
li = list(map(int,input().split(' ')))
for i in range(n-2):
    for j in range(n-1):
        for k in range(n):
            if li[i]+li[j]+li[k] == m:
                print(li[i], li[j], li[k])
            x.append(li[i]+ li[k]+ li[j])
x.append(m)
y = sorted(x)
if m in y:
    print(m)
else:
    print(y[y.index(m)-1])
