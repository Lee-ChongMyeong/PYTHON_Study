# 가변인자는 콤마 이후의 인수를 전부 튜플로 묶어서 가져옵니다.
# 따라서 집어넣을때는 가장 우측에 가변인자를 배치해야 합니다.
# 가변인자의 우측에 일반인수가 있으면 왼쪽에 있는 가변인자가 모든
# 요소를 가져가버려 값을 전달받지 못하는 인자가 발생합니다.
# 따라서 여러 인자를 설정시 가변인자를 가장 오른쪽에 배치해야 합니다.

def add_num2(s, *nums):
    print(s)
    sum = 0
    for num in nums:
        sum += num
    return sum
print(add_num2(3, 6, 9, 12))


