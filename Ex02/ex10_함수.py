




def plus(a, b):
    sum = a+b
    return sum


result = plus(3, 5)
print(result)



#정의 - 여긴 순서 대로 진행 정의를 먼저
def pl(a, b):
    print(f"{a} {b}")

# 실행
pl(3,"입니다")



# 매개 변수와 리컨이 없는 경우
def my_function():

    print("Hello world")

my_function()

print(type(my_function()))


# 내용이 없는 경우
def nonefunction():
    pass

nonefunction()



# return 문이 없는 경우
def my_function():

    print("Hello world")

my_function()

print(type(my_function()))




# 1개 이상의 값을 return 할 수 있다
# def sum_and_mul(a, b):

#     return a+b, a*b

def sum_and_mul(a, b):

    sum = a+b
    mul = a*b

    return sum, mul

print(sum_and_mul(5, 4))

sumNum, mulNum = sum_and_mul(3, 9)

print(sumNum)
print(mulNum)



# 매개변수에 기본값을 지정하여 정의할 수 있다.
def plusPrint(a=0, b=0):

    print(f"a={a}, b={b} 이고 합은 {a+b} 입니다.")

plusPrint()
plusPrint(30)

# plusPrint(, 70) #오류

plusPrint(b=70)

plusPrint(b=100, a=200)





print('========================================')


# 정의
def plus_print(a, b):
    print(a, b)


plus_print(3, 5) # 파라미터를 위치로 매칭
# plus_print(3)
# plus_print()

print('========================================')

# plus_print(,333) #오류
# plus_print(b=333) # 파라미터를 이름으로 매칭
plus_print(b=333, a=2) # 파라미터를 이름으로 매칭




# 정의

#매개변수의 개수를 정의할 수 없을때 - requestBody????
def sum_many(*args): # *를 찍으면 묶여서 온다

    sum = 0

    for num in args:

        sum = sum + num

    return sum

print(sum_many(1,2))
print(sum_many(1,2,3,4,5))


# 다른 매개변수와 함께 사용할때

def sum_mul(mode, *args):

    if mode == "sum":

        result11 = 0

        for i in args:

            result11 = result11 + i

    elif mode == "mul":

        result11 = 1

        for i in args:

            result11 = result11 * i

    return result11


print(sum_mul("sum", 1,2,3,4,5))
print(sum_mul("mul", 2,3))

###### result11 가 정의 되지 않았는데 자연스럽게 밖에 서 쓰인다 뭐임? 
# 위에 result 가 쓰여서 result11로 바꿈
# 자료 형이 정해지지 않아서 
# 자유도가 높아서

# 안에서 선언했는데 나가면 없어지자나 근데 왜 쓸수 있슴?


print('========================================')
# 정의되지 않은 매개변수는 key=value 형태로 전달하면 
# 딕션어리 형태로 받아 처리한다.
def addPerson(hp, **kwargs):

    print(hp)
    print(kwargs) # 타입 딕션어리

addPerson("010-222-3333", name="홍길동", age=28)
print()


print('========================================')
# 다른매개변수와 같이 사용할때는 가장 마지막에 와야한다.
def addPerson2(*hp, **kwargs):

    print(hp) # 타입 튜플
    print(hp[0])

    print(kwargs) # 타입 딕션어리
    print(kwargs['name']) # 딕셔너리는 반복문 못돌림 키로만 뽑음 _keys!!
    

addPerson2("010-222-3333", name="황일영", age=28)
print()
addPerson2("010-222-3333","02-333-3333", name="황일영", age=28)
print()
addPerson2("010-222-3333","02-333-3333", "02-456-6434", name="황일영", age=28)









print('========================================')
# lambda
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, numbers))
print(squared, type(squared))

# def:
# 복잡한 함수, 여러 줄의 코드, 조건문, 루프 등을 포함할 수 있습니다.
# 반환값이 필요할 경우 return 문을 사용합니다.
# 일반적으로 프로그램에서 자주 사용되며, 
# 재사용이 필요한 복잡한 기능을 구현하는 데 사용됩니다.
# 이름이 명확하고, 여러 줄을 포함할 수 있어 가독성이 좋습니다. 
# 문서화(docstring)와 주석을 추가할 수 있습니다.

# lambda:
# 단일 표현식만 포함할 수 있으며, 반드시 하나의 값을 반환합니다.
# return 문을 사용할 필요가 없습니다.
# 주로 다른 함수의 인수로 전달할 때 사용됩니다. 
# 예를 들어, map(), filter(), sorted() 등의 함수에서 
# 간단한 작업을 수행할 때 유용합니다.
# 간단한 작업을 빠르게 처리할 수 있지만, 
# 복잡한 로직이 포함될 경우 가독성이 떨어질 수 있습니다.

# def는 복잡하고 재사용 가능한 함수를 정의할 때 적합하고, 
# lambda는 짧고 간단한 함수를 간편하게 정의할 때 유용합니다. 
# 따라서 상황에 따라 적절한 방법을 선택하여 사용하는 것이 좋습니다




# 문서화(docstring)