# n = int(input())
# honey = list(map(int,input().split(' ')))

n = int(input())
ans = 0
a = list(map(int, input().split()))
s = []
s.append(a[0])

for i in range(1, n):
    s.append(s[i - 1] + a[i])

for i in range(1, n - 1):
    ans = max(ans, s[n - 2] - a[0] + a[i])

for i in range(1, n - 2):
    ans = max(ans, s[n - 1] - a[0] - a[i] + s[n - 1] - s[i])

for i in range(1, n - 1):
    ans = max(ans, 2 * s[i - 1] + s[n - 2] - s[i])

print(ans)

