n = int(input())
color = list(input())
color.append('A') # line 12와 line 21의 arr[i+1] 에서 list의 범위를 벗어나는 오류를 해결하기 위한 방법

cnt = [1] * 2 #파란색을 먼저 칠할 경우와 빨간색을 먼저 칠할 경우의 수를 다 파악하기 위해 cnt를 2개 지정

for i in range(n): #먼저 다 파란색으로 칠했다고 가정한 경우
    if color[i] == 'B':
        continue
    elif color[i] == 'R':
        cnt[0] += 1
        if color[i+1] == 'R':
            cnt[0] -= 1
            continue

for i in range(n): #먼저 다 빨간색으로 칠했다고 가정한 경우
    if color[i] == 'R':
        continue
    elif color[i] == 'B':
        cnt[1] += 1
        if color[i+1] == 'B':
            cnt[1] -= 1
            continue

print(min(cnt)) #두가지 가정 중 가장 작은 값

