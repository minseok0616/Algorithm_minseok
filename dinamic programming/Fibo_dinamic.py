# 다이나믹 프로그래밍은 항상 사용 할 수 있는 것은 아니고, 아래의 2가지 조건을 만족하면 사용할 수 있다.
# 1. 큰 문제를 작은 문제로 나눌 수 있다.
# 2. 작은 문제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다.
# 피보나치 수열은 위의 조건을 완벽하게 만족하는 문제이다.
# 이번에 피보나치 수열을 구현 할때는 메모이제이션 기법을 사용하여 해결한건데, 메모이제이션은 다이나믹 프로그래밍을 구현하는 방법 중
# 한 종류로 , 한번  구한 결과를 메모리 공간에 메모해두고 같은 식을 다시 호출하면 메모한 결과를 그대로 가져오는 기법이다.
# 실제로 메모이제이션을 구현하는 방법은 한 번 구한 정보를 리스트에 저장하는 것이다.


#한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화
d = [0] * 100

#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 포로그래밍)
def fibo(x):
    # 종료 조건(1 혹은 2일때 1을 반환한다)
    if x ==1 or x ==2:
        return 1
    #만약에 이미 계산한 적 문제라면 그대로 반환함
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과를 반환한다.
    d[x] = fibo(x-1) + fibo(x - 2)
    return d[x]

print(fibo(99))

# 물론 재귀 함수를 사용하면 컴퓨터 시스템에서는 함수를 다시 호출 했을 때 메모리 상에 적재되는 일련의 과정을 따라야 하므로
# 오버헤드가 발생할 수 있다. 이러한 이유때문에 재귀함수 대신에 반복문을 사용하면 오버헤드를 줄일 수 있다.
# 일반적으로 반복문을 사용한 다이나믹 프로그래밍이 더 성능이 좋기 때문이다.
# 다이나믹 프로그래밍을 적용했을 때의 피보나치 수열 알고리즘의 시간 복잡도는 O(N)이다.
# 왜냐하면 F(1)을 구한 다음 이 값이 f(2)를 구하는 데 사용되고 이 f(2)가 f(3)을 구하는데
# 사용되는 일련의 과정을 가지기 떄문이다. 한번 구한 결과는 다시는 구해지지 않는다.
# 시간 복잡도가 O(N)임을 확인하기 위해 함수가 종료될 때 어떤 함수를 호출했는지, 현재의
# 피보나치 수를 출력하도록 코드를 만들면 실제로 그림처럼 호출된다는 것을 알 수 있다.
# 이에 대한 소스코드는 check_fibo.py에서 확인하겠다.