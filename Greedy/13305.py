n = int(input())

path = list(map(int,input().split(' ')))
cost = list(map(int,input().split(' ')))

answer = 0
oil = cost[0]

answer += cost[0] * path[0]

for i in range(1,n-1):
    if oil >= cost[i]:
        oil = cost[i]
    else:
        oil = oil
    answer += oil * path[i]

print(answer)

