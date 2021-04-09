
# datatypestr 03 

# 문자열은 한 줄 문자열과 여러 줄 문자열로 나뉩니다.
# 한 줄 문자열은 ", ' 를 여닫는 용도로 사용하며 같은 줄에
# 여닫는 따옴표가 위치해야 합니다.
# 반면에 여러 줄 문자열은 """, '''을 여닫는 용도로 사용하며
# 여닫는 따옴표가 다른 줄에 위치해도 상관없습니다.

s1 = """여러줄로 문자열 작성하기
여러줄로 문자열 작성하기
여러줄로 문자열 작성하기"""
print(s1)

# 만약 ",' 를 사용함에도 불구하고 여러 줄 문자열을 처리하고 싶다면
# 문장 끝에 \를 붙이고 다음줄로 커서를 내려서 이어서
# 계속해서 작성한다.

s2 = "이번 문자열은\
여러 줄 문자열입니다.\
\n단, \\n을 사용해야 개행이 이루어집니다."
    
print(s2)

# 문자열 병합 기능

s3 = "korea" "japan" "2002"
print(s3)