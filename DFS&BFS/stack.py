stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack)# 최하단 원소부터 출력합니다.
print(stack[::-1])# 최상단 원소부터 출력합니다.

# 파이썬에서 스택을 사용할 때는 별도의 라이브러리를 사용할 필요가 없다. 기본 리스트에서 append()와 pop()메서드를 사용하면 스택 자료구조와 동일하게 동작을 한다.
# append() 메서드는 리스트의 가장 뒤쪽에 데이터를 삽입하고, pop()메서드는 리스트의 가장 뒤쪽에서 테이터를 꺼내기 때문이다.