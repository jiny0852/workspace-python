print("형병환=====================================")



t = (1, 2, 3) # 읽기 전용
print(t, type(t))

l = list(t)
print(l, type(l))

l[1] = 100
print(l)


a = [1, 2, 3]
print(a, type(a))

t_tuple = tuple(a)
print(t_tuple)

#t_tuple[1] = 999



print("tuple --> set=====================================")


t = (1, 2, 3, 1)
print(t)

s = set(t)
print(s, type(s))


l = list(s)
print(l, type(l))


t = tuple(l)
print(t, type(t))




























