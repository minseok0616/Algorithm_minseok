#앞서 계산된 결과를 저장하기 위한  DP 테이블 초기화
d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] =2
n = 99

#피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i - 1] + d[i -2]

print(d[n])

# 탑다운 방식은 하향식이라고도 하며, 보텀업 방식은 '상향식' 이라고도 한다.
# 다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식이다. 보텀업 방식에서 사용되는
# 결과 저장용 리스트는 'DP테이블' 이라고 부르며, 메모이제이션은 탑다운 방식에 국한되어
# 사용되는 표현이다