# while문은 조건문과 조합해서 조건문이 "참"이면 실행하고
# 거짓인 경우 탈출하는 반복문이다.
# 실행 및 종료 여부는 반드시 조건식 비교를 통해서만 결정할 수 있다.
# 일단 한 번 실행이 되면 모든 실행문이 실행완료되기 전까지 조건식의
# 참 거짓 여부는 실행 중 중단 여부에 영향을 미치지 못한다.

student = 1
while student <= 5:
    print(str(student) + "번 학생의 출석을 체크합니다.")
    student += 1