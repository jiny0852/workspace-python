
from phonedao import *

start_system = True
while start_system :

    print("*"*50)
    print("전화번호 관리 프로그램")
    print("*"*50)

    status = True

    while status :

            print("1.리스트 2.등록 3.삭제 4.검색 5.종료")
            print("-"*38)
            menu = int(input(">메뉴번호:"))

            match menu :
                 
                case 1 :
                    i = 0
                    person_list = get_list()

                    for person in person_list :
                        print(person_list[i])
                        i += 1

                case 2: #등록
                    pass
                case 3: #삭제
                    pass
                case 4: #검색
                    pass
                case 5: #종료
                    print("*"*50)
                    print("감사합니다")
                    print("*"*50)
                    start_system = False
                    status = False
                
                      






