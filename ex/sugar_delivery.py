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
cnt_3 = 0

while(n>=0):
    if n%5 == 0:
        min_num = cnt_3 + n/5
        break
    else:
        cnt_3 = cnt_3+1
        n = n-3
if min_num == 5000:
    print(-1)
else:
    print(min_num)