# set


print("set 생성=====================================")

no_list = {1, 2, 3}
print(no_list, type(no_list))

print(len(no_list))
print(2 in no_list)
print(2 not in no_list)



print("set 메소드=====================================")

no_list.add(4)
print(no_list)

no_list.add(1)
print(no_list)

no_list.discard(2) # 값 2 가 삭제됨 값이 없으면 지우지 않음 에러x
print(no_list)

no_list.remove(3) # 값 3 이 삭제됨 값이 없으면 에러발생
print(no_list)

no_list.update({2, 3})
print(no_list)

no_list.clear()
print(no_list)



print("set 집합개념=====================================")


s1 = set([1, 2, 3, 4, 5, 6, 7, 9, 10])
s2 = set([10, 20, 30])

print(type(s1), type(s2))


#s3 = s1.union(s2) #합집합
s3 = s1 | s2

print(s3)


#s4 = s1.intersection(s2) #교집합
s4 = s1 & s2

print(s4)


# s5 = s1.difference(s2) #차집합
s5 = s1-s2

print(s5)


s6 = s2-s1

print(s6)












