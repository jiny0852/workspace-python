# 복소수형

a = 4 + 5j
print(a)
print(type(a))
print(isinstance(a, complex))



b = 4 + 5j
c = 7 - 2j
print(b + c)
print(type(b+c))
print(b.real, b.imag)



d = 5 #정수 --> 복소수
print(type(d))
print(complex(d))



#정수 🡪 실수
print(float(d))



e = 7.0 #실수 --> 복소수
print(type(e))
print(complex(e))

#실수 🡪 정수
print(float(e))
print(int(e))







