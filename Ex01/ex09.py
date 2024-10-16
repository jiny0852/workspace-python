# 문자열


s = ''

str1 = 'hello world'
str2 = "안녕 세상"
print(s, str1, str2) # _ hello world 안녕 세상
print(type(s), type(str1), type(str2)) # <'str'> <'str'> <'str'>
print(isinstance(str2, str)) # True


#str3 = "나는 "정우성"입니다."
str3 = "나는 '정우성'입니다." # 작은따옴표 사용
str3 = "나는 \"정우성\"입니다." # 이스케이프문자 사용
print(str3) # 에러발생

#str4 = '나는 '박명수'입니다.'
str4 = '나는 "박명수"입니다.' # 작은따옴표 사용
str4 = '나는 \'박명수\'입니다.' # 이스케이프문자 사용
print(str4) # 에러발생



print('=============================================')

s01 = 'bbb'
s02 = 'bbb'
print(id(s01))
print(id(s02))



print('=============================================')


str5 = """ABCDEFG
abcdef
"가나다"라마
'123'456789"""

print(str5)



str6 = '''ABCDEFG
abcdef
"가나다"라마
'123'456789'''

print(str6)



print('=============================================')



print('Hello\nWorld\nI\'d Say "hello World"')   # '' 을 기본으로 사용
print("Hello\nWorld\nI'd Say \"hello World\"")  # "" 을 기본으로 사용
print("Hello\rWorld") # z커서가 현재줄의 맨앞으로 간다
print("Hello\bWorld") # 커서가 한칸씩 앞으로 간다
print("Hello\tWorld")








