
import sys
for _ in range(int(sys.stdin.readline())):
    N = sys.stdin.readline()
    tmp=list(map(int,sys.stdin.readline().split()))
    print(min(tmp),max(tmp))