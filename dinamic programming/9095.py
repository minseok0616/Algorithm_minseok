n = int(input())

def sum_it(x):
    if x == 1:
        return 1

    elif x == 2:
        return 2
    elif x == 3:
        return 4
    else:
        return sum_it(x-1) + sum_it(x-2) + sum_it(x-3)

for i in range(n):
    x = int(input())
    print(sum_it(x))
