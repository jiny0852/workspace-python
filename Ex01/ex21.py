



# for no in range(1,10,1):
#     print(f"5 * {no} = {no*5}")




# for no in range(2,10,1):
#     for num in range(1,10,1):
#         print(f"{no} * {num} = {no*num}")
#     print()





fruitList = ["red", "orange", "yellow", "green", "blue"]

for color in fruitList:
    print(color)


for index, color in enumerate(fruitList):
    if index > 3:
        break
    else :
        print(index, color)




print("---------------------------------------------")



# students라는 리스트가 있습니다. 
# 학생 이름과 점수가 담긴 리스트입니다. 
# 이 리스트에서 최대 4명의 학생 이름과 점수를 출력하세요.

students = [('철수', 85), ('영희', 92), ('민수', 78), ('지수', 88), ('상철', 90)]

for index, person in enumerate(students):
    if index > 4:
        break
    else :
        print(index, person)


# fruits라는 리스트가 있습니다. 
# 이 리스트에서 5개까지만 과일 이름과 인덱스를 출력하세요.

fruits = ['사과', '바나나', '체리', '포도', '오렌지', '망고', '키위']

for index, name in enumerate(fruits):
    if index > 5:
        break
    else :
        print(index, name)



# weather라는 리스트가 있습니다. 
# 이 리스트는 일주일 동안의 날씨를 나타냅니다. 
# 최대 3일의 날씨를 인덱스와 함께 출력하세요.

weather = ['맑음', '흐림', '비', '눈', '바람']




# hobbies라는 리스트가 있습니다. 
# 이 리스트에서 친구의 취미를 최대 4개까지 출력하세요.

hobbies = ['독서', '운동', '영화 감상', '여행', '요리']




# lunch_menu라는 리스트가 있습니다. 
# 이 리스트에서 오늘의 점심 메뉴를 3개까지만 출력하세요.

lunch_menu = ['김밥', '떡볶이', '비빔밥', '치킨', '피자']









