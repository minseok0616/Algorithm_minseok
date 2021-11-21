n = int(input())
num  = n
count = 0
while(True):
        a = num //10
        b = num % 10

        c = (a+b) % 10
        num = 10*b + c
        count += 1


        if n == num:
                break

print(count)



