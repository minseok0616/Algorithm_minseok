def prime_number(x):
    for i in range(2,x):

        if x % i == 0:
            return False
        return True

n,m = map(int,input().split())
k = list()
for i in range(n,m+1):
    if prime_number(i) == True:
        k.append(i)

print(sum(k))

