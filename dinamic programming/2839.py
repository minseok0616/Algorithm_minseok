n = int(input())
sugar = 0

while n >= 0:
    if n % 5 == 0:
        sugar += n // 5
        print(sugar)
        break
    n -= 3
    sugar += 1
else:
    print(-1)