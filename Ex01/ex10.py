# 문자열의 연산
# 파이썬은 보고서 쓴다고 생각하기!!!!!!!!!


str1 = "FirstString"
str2 = "SecondString"
print(str1 + str2) # FirstStringSecondString


str1 = "FirstString"
print(str1*3) # FirstStringFirstStringFirstString


print("=" * 50)
print("My Program")
print("=" * 50)



print('=======================================')


str = "First String"
print(str[0], str[2], str[5], str[6], str[11]) # F r _ S g # +인덱스
print(str[-12], str[-10], str[-7], str[-6], str[-1])
print(str[0], str[-0]) # 두개의 값은 같다

print(str[0], str[1], str[2], str[3]) # F i r s
print(str[0]+str[1]+str[2]+str[3]) # Firs

print(str[-12], str[-11], str[-10], str[-9]) # F i r s
print(str[-12]+str[-11]+str[-10]+str[-9]) # Firs


print('=======================================')


print(str[0]+str[1]+str[2]+str[3]+str[4])
print(str[-12]+str[-11]+str[-10]+str[-9]+str[-8])

print(str[0:5])
print(str[ :5])
print(str[-12:-7])



print('=======================================')


print(str[6]+str[7]+str[8]+str[9]+str[10]+str[11])
print(str[-6]+str[-5]+str[-4]+str[-3]+str[-2]+str[-1])


print(str[6:12])
print(str[6: ])
print('=======================================')
print(str[-6:-0])  # 여기는 표현 안됨
print(str[-6:0])  # 여기는 표현 안됨
print(str[-6:-1])  # strin
print(str[-6:1])  # 여기는 표현 안됨
print(str[-6:len(str)]) # string 쳇지피티가 시킴
print('=======================================')


print(str[1:9:3]) # 1번부터 9번까지 3칸씩 itt
print(str[3:3]) # 여기는 표현 안됨
print(str[3:]) # 3부터 끝까지
print(str[:]) # 처음부터 끝까지
print(str[-6:-2])
print(str[::-1]) # 문자열을 역으로 츨력한다   처음부터 끝까지 2개씩 이동 뒤집혀서 배열이 뒤집힘




print()
print()
print()
print()
print('=======================================')
#str[7] = 'A' # 문자열의 중간값만 변경할 수 없다 
# str을 걍 바꿔버리면 된다

name = "길동"
age = 40
#print( name + age ) # 문자열 객체와 정수형 객체는 + 연산을 할 수 없다.


name = "이효리"
print(name[::-1])







