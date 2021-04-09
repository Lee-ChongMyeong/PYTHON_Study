# 5. <문자열 자료 : Escape(이스케이프) 제어 문자>
# 이스케이프란? 문자열 안에 " \문자 " 로 표기하며, print 가 하지 못하는 기능을 문자로 제어
# 이스케이프 표기 : "\n" (엔터 문자), "\t"(Tab키), "\b" (백스페이스키)
# ' \" ' 는 "문자열 표기"
# ' \' ' 는 '문자열 표기
# " \\"  는 \문자열 표기

# 5_1) 이스케이프 예시)
print("Escape\n이스케이프 문자는\n")
print("문자열에서만 사용 가능합니다.")
print()     #print()로 "화면 출력에 엔터로 사용"
print("12345678123456781234567812345678")
print("tab\tstart\tshift\tend")
print("!\t시작\t커서이동\t끝")
# tab은 기본 8칸 공백(스페이스바)로 일정한 간격을 맞춤.
# 문자열에 들어가는 문자는 각각 한 칸씩 1Byte 공간을 차지
# 단, 한글은 무조건 두칸(2Byte)
# 소스파일 자체의 공백과 tab키는 "들여쓰기"
print("abcd\b123")  #"\b"는 커서를 한칸 왼쪽으로 이동, 뒤에 공백 한 칸 필요
print("abcd\b")
print("abcd\b ")    
print('문자열에 \'작은 따옴표 \'출력')
print("문자열에 \"큰따옴표\"출력")
print("문자열에 \\표현")

# 예외
print("문자''가능")
print('큰따옴표"가능')
print("문자열에 \표현")

print("문자열에 \test")
print("문자열에 \\test")

# 5_2) 연산의 예외 <문자열 연산>
# 문자열 연산: 더하기[문자열 + 문자열]
print("최" + "강")
print('1' + "2.12")
print(1 + 2.12)
## print(1 + '2.12')       #Error : +연산자 -> 숫자는 숫자끼리, 문자열은 문자열 끼리

# 문자열 연산 : 곱하기 [문자열 * 숫자(자연수)]
## print("최" * "강")   #Error
print("최" * 5)
print(5 * '*')
## print(3.14 * '*')    # 실수형으로는 지원안됨. 무조건 정수


# 5_3) print()함수에서 사용 가능한 내장 함수 (sep, end)

# 5_3_1)sep(separation)은 문자열에서 구분자 쉼표(,) 를 화면 출력시 원하는 걸로 변경시켜주는 기능
print("010-1234-5678")
print("010","1111","2222")
print("010","1111","2222", sep="-")

# 5_3_2)
# end는 print()와 그 다음 print()에 있는 내용들을 이어서
# 한 줄에 출력하고 싶을 떄 사용(end는 주로 print의 엔터를 없애는 기능)
print("나는"); print("최강이다.")
print("나는", end=" "); print("최강이다.")

print(1, end=',')
print(2, end=',')
print(3)

