print(bin(int(input(), 8))[2:])

# int() 안에 input() 다음에 , 를 찍고 숫자를 입력하면 그 진법으로 숫자를 입력 받는다는 것을 의미하게 된다.
# 그리고 2진법을 의미하는 bin(ary)으로 감싸주면 2진법 숫자가 된다. 변환된 이후에는 맨 앞 2자리에 이진법을 의미하는 0b가 붙기
# 때문에 2번째 자리 부터 출력 될 수 있도록 [2:]를 붙여주면 된다.