# 이효리,010-2222-3333,031-2323-4441
# 정우성,010-2323-2323,02-5555-5555
# 이정재,010-9999-9999,02-8888-8888


# 파일 한번에 읽기
file_path = "C:\\javaStudy\\workspace-python\\Ex02\\PhoneDB.txt"



file = open(file_path, "r", encoding="utf-8")
data = file.read()
print("전체 읽기")
print(data)
file.close()


# 파일 한줄씩 읽기
print("파일 한줄씩 읽기")

file = open(file_path, 'r', encoding="utf-8")
for line in file:
    print(line.strip())   # .strip() 줄바꿈,공백,탭 삭제
file.close()



# 파일 한줄씩 읽기2    "블럭" 단위
print("파일 한줄씩 읽기2")
with open(file_path, 'r', encoding="utf-8") as file:
    data = file.read()
    print(data)


# 블럭이 끝나면 자동으로 클로즈됨 file.close()안쓰려고 하는것임

# with 문은 파일 입출력, 데이터베이스 연결, 네트워크 소켓 등 리소스를 
# 안전하게 관리하기 위해사용된다.

# 리소스를 자동으로 닫아주어 코드가 간결해지고, 리소스 누수를 방지할 수 있다.

# with 문을 사용하면 리소스 관리가 더 간편해진다.










