#10_5)윤년을 구하는 코드 [윤년? 약 4년씩 2월 29일이 있는 해]
# 조건1) 4의 배수는 윤년이 된다. 그 외는 평년
# 조건2) 4의 배수면서 100의 배수인 경우는 평년이다. 그 외는 윤년
# 조건3) 4 그리고 100의 배수이면서 400의 배수인 경우 윤년이다. 그 외는 평년

#10_5_1) 단순 if문만
# year = int(input("년도 입력 : "))
# if year % 4 == 0 and year % 100 != 0:
#     print("1) 윤년")
# if year % 100 == 0 and year % 400 != 0:
#     print("2) 평년")
# if year % 400 == 0:
#     print("3)윤년")
# if year % 4 != 0:
#     print("1)평년")

#10_5_2) if ~ else 문?      # 불가능..\

#10_5_3)
year = int(input("년도 입력 : "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("윤년")
        else:
            print("평년")
    else:
        print("윤년")
else:
    print("평년")
    
#10_5)윤년을 구하는 코드 [윤년? 약 4년씩 2월 29일이 있는 해]
# 조건1) 4의 배수는 윤년이 된다. 그 외는 평년
# 조건2) 4의 배수면서 100의 배수인 경우는 평년이다. 그 외는 윤년
# 조건3) 4 그리고 100의 배수이면서 400의 배수인 경우 윤년이다. 그 외는 평년

#10_5_4) 다중 if 문
year = int(input("년도 입력 : "))
if year % 400 == 0:
    print("3) 윤년")
elif year % 100 == 0:
    print("2) 평년")
elif year % 4 == 0:
    print("1)윤년")
else:
    print("1)평년")
