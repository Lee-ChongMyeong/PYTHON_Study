# print
# - 출력함수
#   > 화면에 출력 할 내용을 print() 괄호 안에 작성

# data가 문자라면 작은따옴표 or 큰따옴표로 묶어주어야 한다.
'''
print('hello')
print('hello python')
print("hello")
'''
# print(hello python)   error code

# C언어와 다르게 Python 에서는 print 마지막에 enter 가 들어간다.

# 주석
# 컴퓨터가 (python이) 특정 코드를 읽지 못하게 만드는 기호

# 한 줄 주석 : # 
# # 기호 뒤쪽으로 입력한 내용은 python이 읽어내지 않는다.

# 문단 주석 : '''   '''     or  """     """
# 작음따옴표/큰따옴표 3개 묶음으로 열고 닫아 사용
# 그 사이의 내용을 python이 읽어내지 않는다.

'''
print('hello'   # 한줄로만 표현된다.
      'python'  # 줄 마다 따로 '' 묶어줘야 된다.
      'world'
)
'''
# ;
# ; (세미콜론) 기호는 여러 줄이 작성되어야 하는 내용을 한 줄로 작성할 때 사용
'''
print('큰따옴표 안의 내용 출력'); print('이어 쓰기 활용'); print('; <- 세미콜론')
'''
# escape 문자

# \ (역슬래시, / 기호 x ) 기호 뒤에 다른 문자를 붙여서 
# 특정 동작을 수행하도록 예약되어 있는 문자

# \n

# 개행문자, print 내부의 내용이 출력되다가 \n 을 만나면 enter가 입력된다.
# (다음줄로 넘어가서 남은 내용이 출력된다)
'''
print('hello python')
print('hello'); print('python')
print('hello\npython\ntest')
'''

'''
# ex)
print('저의 이름은 이총명입니다.\n저의 나이는 24살입니다. \n주소는 산골짜기 입니다.')
'''

# \t

# 내용이 출력되다가 \t를 만나면 tab이 눌러진다.
# (출력되는 내용에 tab을 넣어준다)
'''
print('Have\ta\tGood\tTime')
print('1234567\t1\t12345678\t123')
'''

# \' \"
# 큰 따옴표 안에서 큰 따옴표를 출력할 때
# 작은 따옴표 안에서 작은 따옴표를 출력할 때 사용

# 아버지께서 '너 집에 들어는 올거냐?' 라고 물어보셨다   <<< 출력하고 싶은 문장
# print("아버지께서 '너 집에 들어는 올거냐?' 라고 물어보셨다")  << 정상 동작    print 안을 " "로 묶음
# print('아버지께서 '너 집에 들어는 올거냐?' 라고 물어보셨다')  << error
#       ^          ^                     ^               ^
#      열고        닫고                  열고             닫고

'''
print("큰 따옴표 안에서 큰 따옴표 출력 \" ")
print("큰 따옴표 안에서 작은 따옴표 출력 ' ")
print('작은 따옴표 안에서 큰 따옴표 출력 " ')
print('작은 따옴표 안에서 작은 따옴표 출력 \' ')
'''

# \\ 
# \ 자체를 escape 문자로 사용
# \ 뒤에 다른 문자가 붙어 있으면 의도하지 않은 escape 문자로 사용 될 수 있다.
# 그래서 \ 기호 뒤에 다른 문자를 붙인 형태를 출력하고 싶을 떄는 \\ 형태로 사용

print('표현 \ 방식')
print('표현 \2 방식')   # \2 가 없어져 버림, 존재하지 않는 escape 인데 동작해버림
print('표현 \\2 방식')
# print('표현 방식 \') #error code [열었는데 닫는게 없음.]
print('표현 방식 \\')

print('\ 20,000')
print('\20,000')
print('\\20,000')

# print 함수를 이용하여 숫자를 출력할 때
# > 작은따옴표/ 큰 따옴표로 묶어 주지 않는다.
# (묶으면 문자 취급, 안 묶으면 숫자 취급)

print('123')
print(123)

print('123 + 123')
print(123 + 123)
print(2 * 23)
print(120 /3)

# 문자와 숫자를 이어서 입력 할 때에는, (콤마) 기호를 사용




