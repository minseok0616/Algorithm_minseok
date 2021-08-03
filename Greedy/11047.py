a,b = list(map(int,input().split(' ')))

coin_list = []
count = 0
for i in range(a):
    coin_list.append(int(input()))
coin_list.sort(reverse =True)
for coin in coin_list:
    count += b // coin
    b %=coin
print(count)
