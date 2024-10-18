

pi = 3.14

def plus(a, b):
    return a+b

def minus(a, b):
    return a-b

def multi(a, b):
    return a*b

def div(a, b):
    return a/b

def area_circle(r):
    return pi*r**2


print(plus(55, 66))


print(area_circle(5))





# 집적 실행
print("=========================================")
# print(__name__)    # __main__"

# print(55, 66)

# 본인이 실행하면 __main__
# 남이 부르면 --> 파일명 

# 이파일을 실행일때만 실행됨    남이 부르면 실행 되지 않는 부분
if __name__ == "__main__" :
    
    print(plus(30,10))
    print(minus(30,10))
    print(multi(30,10))
    print(div(30,10))
    print(area_circle(5))
    print(__name__)

















