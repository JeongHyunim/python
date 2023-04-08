import sys 

for i in  range(3):
    lst = list(map(int, sys.stdin.readline().split()))

    if sum(lst)==3:
        print("A")
    elif sum(lst)==2:
        print("B")
    elif sum(lst)==1:
        print("C")
    elif sum(lst)==0:
        print("D")
    else:
        print("E")