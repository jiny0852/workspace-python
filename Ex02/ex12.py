


num = int(input("숫자를 입력하세요 : \n"))

try:
    result = 100/num
    print(result)   

except ZeroDivisionError as e :
    print(f"예외 발생: {e}") # 예외 메시지 출력

except FileNotFoundError as e :
    print()

# finally 블록은 파이썬의 예외 처리 구조에서 선택적으로 사용할 수 있습니다.
finally :  
    # 예외 발생 여부와 상관없이 무조건 실행되는 문장
    # 공통영역
    print("공통영역 - 이 블록은 항상 실행됩니다.")

    # //정상적이거나? 
    # 잡지 못한 에러를 여기서 더블 체크 한다
    # file.close() 같이 


print("프로그램 정상 종료")



# 예외 발생 시 후속 처리가 필요한 경우
# finally 블록이 필요한 이유는 다음과 같습니다:

# 자원 정리: 파일이나 네트워크 연결을 닫아야 할 때 유용합니다.
# 로그 기록: 예외 발생 여부와 관계없이 로그를 남길 필요가 있을 때 사용됩니다.
# 후속 작업: 예외가 발생했는지에 상관없이 수행해야 하는 작업을 포함할 수 있습니다.
# 따라서 finally 블록이 없으면, 예외 처리 후 무조건 실행되어야 하는 코드가 실행되지 않으므로, 
# 프로그램의 안정성이나 자원 관리 측면에서 불리할 수 있습니다.















