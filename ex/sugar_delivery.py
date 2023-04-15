# n = int(input())
# min_num = 5000
# for i in range(n//3 +1):
#     for j in range(n//5 +1):
#         if ((i*3+j*5  == n) and (i + j <min_num)):
#             min_num = i + j

# if min_num == 5000:
#     print(-1)
# else:
#     print(min_num)

n = int(input())
min_num = 5000
a = n//5
b =n%5
c = 0
if n%5 == 0:
    print(n)
while True:
    if b % 3 == 0:
        c = b//3
        b = b%3

        break
    b = b + 5
    a = a-1
print((b == 0)and(a+c) or -1)