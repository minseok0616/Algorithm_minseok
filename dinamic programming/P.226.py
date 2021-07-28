n,m = list(map(int,input().split(' ')))

k = list(map(int,input().split(' ')))

dp = [10001]*10001
dp[0] = 0
for i in range(n):
    for j in range(k[i],m+1):
        dp[j]=min(dp[j],dp[j-k[i]]+1)

if dp[m] == 10001:
    print(-1)
else:
    print(dp[m])