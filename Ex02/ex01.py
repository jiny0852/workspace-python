



test_list = [1, 12, 123, 1234]

print(test_list[0], test_list[3])
print(test_list[-1]) # -인덱스


print(test_list[1:3]) # 1번방 부터 (3-1) 번방까지 슬라이싱 문법 가능

print(len(test_list)) # len() 메서드로 갯수 확인

print((test_list * 2)[5])

print(12 in test_list) # 배열에 12가 있으면 true

print('리스트 삭제============================')

# del(test_list[2])
# del test_list[2]
print(test_list)


print('리스트 수정============================')

#test_list[0] = "apple"
print(test_list)

b_list = ["apple", "banana", 10, 20]
# sum = b_list[2] + 90
b_list = b_list[2] + 90
print(b_list)


print(test_list[0:2])
test_list[0:2] = [888, 999]
print(test_list)


test_list[0:2] = [777]
print(test_list)


test_list[2:3] = [111]
print(test_list)


test_list[0:2] = ["aaa", "bbb", "ccc"]
print(test_list)



print('슬라이스를 통한 삭제============================')

a = [1, 12, 123, 1234]
print(a)


a[1:2] = [] # 1번째 방 삭제
print(a)

a[0:] = []
print(a)



print('슬라이스를 통한 삽입============================')

a = [1, 12, 123, 1234]


a[1:2] = ["a"]  # a[1:2] -> a[1:1] 수정개념
print(a)

a[1:1] = ["a"]  # a[1:1] -> a[1:0] 추가개념
print(a)


a[5:] = [12345]
print(a)

#슬라이싱 문법 방번호가 같으면 추가[3:3]


a[:0] = [-12, -1, 0]
print(a)



print('리스트의 메소드 사용============================')

a = [1, 12, 123, "hello", 3.14, 1000]
print(a)

#추가
a.append("정우성")
print(a)


a.insert(2, "박명수")
print(a)


a.extend([6, 7, 8])
print(a)


# 제거

a.remove(1000) # 값으로 찾아서 삭제
print(a)

a.pop(2) # 방번호로 지우기 #del(a[2])
print(a)

a.pop()  # 방번호로 지우기x -->마지막꺼
print(a)


print('222리스트의 메소드 사용222============================')

b = [1, 123, 1000, 12, 1000]
print(b)


# 카운트

print(b.count(1000)) # 리스트에 1000이 몇개있는지


# 뒤집기

b.reverse() # 원본의 리스트 순서가 뒤집힌다
print(b)


# 정렬

b.sort() # 원본 리스트가 오름차순으로 정렬된다
print(b)

b.sort(reverse=True) # 원본 리스트가 오름차순으로 정렬된다
print(b)


# 값으로 index 번호 찾기

print(b.index(1000)) # 처음 검색되는 방번호 리턴






print(type(test_list))

