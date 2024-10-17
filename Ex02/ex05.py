print("패킹과 언패킹=====================================")



t = 10, 20, 30, "python" # 튜플로 묶어서 변수에 할당 * 읽기 전용 리스트

print(t)
print(type(t))

l = list(t)
print(type(l))  # 기본값이 튜풍이라 바 꿀수 없다

# unpacking tuple

a, b, c, d = t
print(a, b, c, d)
print(type(a))

# unpacking list

a, b, c, d = [10, 20, 30, "python"]
print(a, b, c, d)
print(type(b))






























