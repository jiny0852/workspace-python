



num = input("숫자를 입력하세요: \n")

num = int(num)

"""
# 예제
if num > 0 :

    print("양수")

elif num < 0 :

    print("음수")

else :

    print("0입니다.")

"""

# 문제 ifelse01.py
# 숫자를 입력받아 아래와 같이 출력되는
# 프로그램을 작성하세요


"""
if num < 0 :

    print("음수")

elif (num % 2) == 0 :

    print("짝수")

else :

    print("홀수")
"""


# [문제 ifelse02.py]
# 과목번호를 입력받아 강의실 번호를 출력하는
# 프로그램을 작성하세요


# if num == 1 :

#     print("R101호 입니다")

# elif num == 2 :

#     print("R202호 입니다")

# elif num == 3 :

#     print("R303호 입니다")

# elif num == 4 :

#     print("R404호 입니다")


# else :

#     print("상담원에게 문의하세요")


match num:  # break가 기본적으로 있다고 생각
    case 1:

        print("R101호 입니다")

    case 2 :

        print("R202호 입니다")

    case 3 :

        print("R303호 입니다")

    case 4 :

        print("R404호 입니다")

    case _:

        print("상담원에게 문의하세요")






