n = int(input())

red_b = list(map(int,input().split()))

red_b.sort(reverse =True)

result = red_b[0]
for i in range(1,n):
    result += red_b[i]/2

print(result)