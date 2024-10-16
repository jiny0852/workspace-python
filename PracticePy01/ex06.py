


# 상품을 구매하면 정가의 10%를 부가세로 부여한다. 
# 아래와 같이 출력되도록 프로그램을 작성하세요

price = input("상품가격 : \n")
money = input("받은돈 : \n")

tax = float(price)/10


print(f"받은돈 : {float(money)}")
print(f"상품가격 : {float(price)}")
print(f"부가세 : {tax}")
print(f"잔액 : {float(money)-float(price)}")






