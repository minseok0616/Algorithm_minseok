import sys
n = int(input())

m = list(map(int, sys.stdin.readline().split()))
con_fac = []
for i in range(1,min(m)+1):
    if n == 2:
        if m[0] % i ==0 and m[1] % i == 0:
            print(i)
    else:
        if m[0] % i ==0 and m[1] % i == 0 and m[2] % i ==0:
            print(i)




