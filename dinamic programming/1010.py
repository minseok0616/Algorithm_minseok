import math

n = int(input())
for i in range(n):
    n, m = map(int, input().split())  # mCn

    answer = math.factorial(m) // (math.factorial(n) * math.factorial(m - n))


    print(answer)