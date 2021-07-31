# 2원과 5원짜리가 무한정 있고, 동전의 개수가 최소가 되도록 거슬러 줘야한다.
# 거스롬돈이 n인 경우에 최소 동전의 개수가 몇 개 인지 알려주는 프로그램을 작성해라.
# 거슬러 줄 수 없다면 -1 출력

# rest = int(input())
# count = 0
#
# coin_list = [5,2]
#
# for coin in coin_list:
#     count += rest // coin
#     rest %= coin
#
# if rest != 0:
#     print('-1')
#
# else:
#     print(count)

#위의 코드가 작동이 되진않는 경우는 13을 대입해보면 오류가 있음을 알 수 있다.
# 그래서 아래와 같이 풀어보았다.
n = int(input())
if n in [1,3]:
    result = -1
elif n%5%2 ==0:
    result = n//5 + (n%5)//2
else:
    result = ((n//5)-1) + ((n%5+5)//2)
print(result)
