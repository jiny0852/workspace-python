# 확장 연산자

x=2

x+=5
print(x) # x = x + 5 -->7

x-=3
print(x) # x = x - 3 -->4

x**=3
print(x) # x = x**3 -->64



print('-'*50)
# 관계 연산자

print(1 > 3) # False
print(2 < 4) # True
print(4 <= 5) # True
print(4 >= 5) # False
print(6 == 9) # False
print(6 != 9) # True


a = 6
print(0 < a < 10)
print(0 < a and a < 10)




print('-'*50)


a = 10
b = 20
c = a
d = 11
e = 11

#주소값 출력하는 함수 id()

#같는 값은 같은 주소

print(id(a)) # 10-->140735392631512
print(id(b)) # 20-->140735392631832
print(id(c)) # 10-->140735392631512 a와 같은주소

print(id(d)) # 11-->140735392631544
print(id(e)) # 11-->140735392631544 d와 같은주소

# == 값비교 is() 주소값비교

print( a==b ) # False
print( a is b ) # False
print( a is c ) # True
print( a is d) # False
print( d is e) # True


print('-'*50)
a = 11 # a=10 🡪 a=11

print(d is a) # True
print(id(a)) # 10-->140735392631512
print(id(d)) # 10-->140735392631512




print('33'*50)
#논리 연산자

print(True and True) # True
print(False and True) # False
print(True or True) # True
print(False or True) # True
print(not True) # False
# print(!True)

a = 15
print(0 < a and a < 10) # True and False --> False


print('-'*50)
# 내장 수치 함수


print(abs(-3)) # 3 --> 절대값으로
print(int(3.1415)) # 3 --> 정수형으로
print(float("3")) # 3.0 --> 실수형으로
print(complex("3")) # (3+0j) -->복소수형으로
print(pow(2, 10)) # 2**10=1028 -->승수 계산






