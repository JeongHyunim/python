import sys
# num = list(map(int, sys.stdin.readline().split()))
# target = int(input())
# x = []
# for i in range(len(num)):
#     for k in range(i+1,len(num)):
#         if num[i]+num[k] == target:
#             x = [i,k]
#             x = x.sort()
#             print(x)
nums = list(map(int, sys.stdin.readline().split()))
target = int(input())
answer = []
for i in range(len(nums)-1):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print([i,j])

