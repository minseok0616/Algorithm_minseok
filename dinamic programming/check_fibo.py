d = [0] * 100
def pibo(x):
     print('f(' + str(x) + ')', end = ' ')
     if x == 1 or x == 2:
         return 1
     if d[x] != 0:
         return d[x]
     d[x] = pibo(x -1) + pibo(x -2)

     return d[x]
pibo(6)

#이렇게 재귀 함수를 이용하여서 다이나믹 프로그래밍 소스코드를 작성하는 방법을,
# 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 탑다운 방식이라고 말한다.
# 반면에 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을
# 도출 한다고 하여 보텀업 방식이라고 한다.

# 피보나치 수열 문제를 아래에서 위로 올라가는 보텀업 방식으로 풀 수 있는데,
# 동일한 원리를 적용하되 단순히 반복문을 이용하여 문제를 해결한 것으로 이해하면 된다.
# 이를 보기위해 fibo_repeat.py로 가자.