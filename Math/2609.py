from math import gcd

a,b = map(int,input().split())
def lcm(x,y):
    return x*y // gcd(x,y)

print(gcd(a,b))
print(lcm(a,b))
