# 25_3) 계산기 구현 (덧셈)

# 25_3_1) 클래스 없이 함수만 정의한 경우 1) 문제점

res1 = 0
res2 = 0
def add1(n):
    global res1
    res1 += n
    return res1

def add2(n):
    global res2
    res2 += n
    return res2

add1(3)
add2(3) 
print(add1(3))
print(add2(4))

# 만약, 계산기에 숫자 3을 입력하고 + 기호를 입력한 후 4를 입력하면 결괏값으로 7을 보여줍니다.
# 근데, 다시 한 번 + 기호를 입력한 후 3을 입력하면 기존 결괏값 7에 3을 더해 10을 보여준다.
# 즉, 계산기는 이전에 계산한 결괏값을 항상 메모리 어딘가에 저장하고 있다는 겁니다.

# 만일, 3 + 4 = 7, 3 + 7 = 10 두 개를 결과를 하고 싶다면

