n = int(input())

money = list(map(int,input().split(' ')))

money.sort()

num = 0
for i in range(n):
    for j in range(i + 1):
        num += money[j]
print(num)

