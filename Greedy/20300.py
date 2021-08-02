# 운동기구를 최대 2개까지 선택할 수 있다
# 헬스장에 있는 N개의 운동기구를 모두 사용해보고 싶어서 2개씩 전에 안쓴걸 써보기로 함.
# 즉 10개의 운동기구가 있다면 pt를 5번 9개라면 5번 받지만 마지막에는 운동기구를 하나만 사용한다.
# n = int(input())
# muscle_loss = list(map(int,input().split()))
# sum_list = []
#
# for i in range(n//2):
#     sum_list.append(muscle_loss[i] + muscle_loss[n-1-i])
#
# print(max(sum_list))

N = int(input())
T = list(map(int, input().split()))
M = 0
T.sort()

if len(T) % 2 == 0:
    for i in range(N // 2):
        M = max(M, T[i] + T[N - 1 - i])
else:
    for i in range(N // 2):
        M = max(M, T[i] + T[N - 2 - i])
    M = max(M, T[-1])
print(M)