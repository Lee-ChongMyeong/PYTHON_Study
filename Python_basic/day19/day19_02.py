# day19_02.py

# 25_4) 클래스 적용 (실행 x )

# class 햄버거:
#     def 햄버거재료(객체매개변수, 매개변수1 ...):
#         빵, 패티, 양상추 ...
    

# 치즈버거 = 햄버거()     # 치즈버거라는 객체 생성

# print(치즈버거.햄버거재료(인수1, 인수2, ...))       # 치즈버거 안에 재료들 정의한거 호출
# print(햄버거().햄버거재료(인수1, 인수2, ...))

# 25_5_1) 클래스 예시1) 주의
# class 햄버거:
#     def recipe(a, b):
#         print("{}버거는 {}와 {}로 만들기".format(a,a,b))
    
# 햄버거.recipe("치즈", "피클")     # 객체 생성하지 않고 호출만 하는것임.   직접 접근
## 햄버거().recipe("치즈")             # (햄버거라는 이름의) 임시객체      햄버거()로 만들면 객체가 생성되는 것임


# 치즈 = 햄버거()
# 치즈.recipe("치즈")



#클래스 선언한 명으로 직접 접근해서 호출하면, 적용되는데
#객체를 생성 후, 접근하려고하면 TypeError가 뜬다.
#(매개변수는 2개인데, 이상하게 인수는 3개 전달 됬다고 에러뜬다.)
#이 이유는 객체를 생성한 순간, 햄버거().recipe()로 접근할 때,
#이미 햄버거()객체가 매개변수에 전달되기 때문입니다.
#즉, 객체 치즈가 이미 햄버거 클래스 안에 recipe매서드에 '자동 전달' 된 것입니다.  



# 25_5_2) 클래스 예시2) 해결
class 햄버거:
    def recipe(self, a,b):         # self가 객체를 받는 매개변수(객체매개변수)
        print("{}버거는 {}와 {}로 만듬.".format(a,a,b))

치즈버거 = 햄버거() # 객체 생성 == 햄버거()
                   # 햄버거()라는 객체가 생성되고 치즈버거에 저장됨

치즈버거.recipe("치즈", "피클")

치즈 = 햄버거()
치즈.recipe("치즈1", "피클1")

치킨보고 = 햄버거()
치즈.recipe("치킨", "피클1")






