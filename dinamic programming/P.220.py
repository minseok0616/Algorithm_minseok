n = int(input())

k = list(map(int,input().split(' ')))

dp = [0] *  101

dp[0] = k[0]
dp[1] = max(k[0],k[1])
for i in range(2,n):
    dp[i] = max(dp[i-2] + k[i],dp[i-1])

print(dp[n-1])