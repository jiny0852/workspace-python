


# 1~45까지의 숫자 중 임의의 6개의 숫자를 출력하세요-미니로또
# 랜덤함수 검색해볼것
# 중복체크 할 것


import random

# random_integer = random.randint(1, 45)  # 1부터 10까지의 랜덤 정수

# num = 0
# s = set([])

# if num < 6:
#     for num in set:
#         s.add(random.randint(1, 45))
#         #s.add(random_integer)

# print(s)

# 빈 집합 생성
s = set()

# 6개의 고유한 숫자를 생성할 때까지 반복
while len(s) < 6:
    s.add(random.randint(1, 45))  # 1부터 45까지의 랜덤 정수 추가

# 집합을 리스트로 변환하고 정렬
lotto_numbers = sorted(s)

print("선택된 미니로또 번호:", lotto_numbers)


