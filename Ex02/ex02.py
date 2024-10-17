

print('튜플 기본============================')


t = (1, 2, 3) # t = 1, 2, 3 # t = tuple([1,2,3])

print(t, type(t))




t = 1, 2, "python"
print(t, type(t))

print(t[-2], t[-1], t[0], t[1], t[2])
print(t[1:3])
print(t[:])

print(t * 2)
print(t + (3, 4, 5)) # t = t + (3, 4, 5) 이렇게 해야 합쳐짐

print(t)

print(len(t))
print(5 in t)


print('튜플 생성============================')

t = (1, 2, 3, 4)  # 리스트 --> a = [1, 2, 3, 4]

tt = 100, 200, 300
print(tt)

t = ((99)) # 값이 하나만 있을떄는 숫자다
t = (99,)  # 값이 한개일떄 튜플 생성 방법

print(t)


print('튜플 값 변경(x)============================')

t = ("apple", "banana", 10, 20)
# t[0] = "mango"
#t[2] = t[2] + 90
print(t[2]+10)


a_list = list(t)

print(type(t))
print(type(a_list))






