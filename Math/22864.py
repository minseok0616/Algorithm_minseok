a,b,c,m = map(int,input().split())
tired = 0
work = 0
time = 0
while(time < 24):
    if tired < 0:
        tired = 0
    if tired + a <= m:
        tired += a
        work += b
        time += 1
    else:
        tired -= c
        time += 1

print(work)




