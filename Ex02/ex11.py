# 스코핑 룰(Scope)

# 이름공간(Namespace)
# - Local Scope : 함수 내부
# - Global Scope : 모듈 내부
# - Built-in Scope : 내장 영역
# 만일 동일한 이름이 이 세 가지 Scope에 존재하면 LGB 순서로 찾는다.


x = 5                 # global 글로벌

def calPlus(no):
    return no+x

print(calPlus(10))
# LGB 규칙에 따라 Local에서 찾을 수 없기 때문에 Global(모듈) 영역에서 x를 찾는다.

print('================================')

def calPlus2(no):       # local 로컬
    x = 1               # x 가 새로 만들어진건지 선언된건지 인식 어려움 젤 가까운거씀
    return no+x

print(calPlus2(10)) 
# LGB 규칙에 따라 Local 영역에서 x를 찾는다.


print('================================')

# 블록 스코프 --> 람수 스코프  안에서 생긴거는 계속 살아있슴 블록이 아니라 "함수"임 
# 자료형이 최소 단위가 아니라 "함수"가 최소단위인거임

def calPlus3(mode, no):       # local 로컬
    
    if mode == 1:
        sum = no + 1       # block 블록 if{블록영역} else{블록영역}??????
    elif mode == 2:
        sum = no + 2
    else :
        print("에러")
                
    return sum

print(calPlus3(10)) 
# 함수 내부에서 전역 객체(외부변수)를 사용해야 하는 경우 global 선언문을 사용한다.









