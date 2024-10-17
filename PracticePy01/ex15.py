


# 5개의 숫자를 키보드로 입력받아 평균을 구하는 프로그램을 작성하세요.


# 빈 리스트 생성
numbers = []

# 5개의 숫자를 입력받기
for i in range(5):
    num = float(input(f"{i + 1}번째 숫자를 입력하세요: "))  # 입력받은 값을 실수로 변환
    numbers.append(num)  # 리스트에 추가

# 평균 계산
average = sum(numbers) / len(numbers)  # 리스트의 합을 리스트의 길이로 나눔

# 결과 출력
print(f"입력한 숫자들의 평균: {average}")







# list = ["", "", "", "", ""]
# list = []

# result = 0
# num = 0  

# if num < 5:


#     for count in list :
#         count = int(input("숫자를 입력해주세요\n"))
#         list.append(count)
#         num +=1


    

#for num in list:

#print(list)

# print(f"주어진 배열에서 3의 배수의 갯수=>{count}")
# print(f"주어진 배열에서 3의 배수의 합=>{result}")


