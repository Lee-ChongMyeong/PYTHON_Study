# 이차원 데이터 처리 예시
# 아파트 한 동에 대해서 신문을 배달할지 말지에 대해서
# 판단할 수 있는 반복문 작성

rooms = [[101, 102, 103, 104],
        [201, 202, 203, 204],
        [301, 302, 303, 304],
        [401, 402, 403, 404]]

nodeliver = [102, 204, 303, 401]

# 중첩 반복문을 이용해서 room 전체를 조회하되
# nodeliver에 포함된 번호는 "요금 미납 세대 %d호입니다."를 출력
# 그렇지 않은 번호는 "%d호에 신문을 배달했습니다." 라고 출력하도록
# 중첩 반복문을 구성해주세요.

# 내가한 답
# index = 0

# for x in rooms:
#     for y in x:
#         if(y == nodeliver[index]):
#             print("요금 미납 세대 %d호입니다." %nodeliver[index])
#         else:
#             print("%d호에 신문을 배달했습니다." %y)
#     index += 1       

for floor in rooms:
    for room in floor:
        if room not in nodeliver:
            print("%d호에 신문을 배달했습니다." % room)
        else:
            print("요금 미납 세대 %d 호 입니다." % room)
    