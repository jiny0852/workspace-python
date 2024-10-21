
from phonedao import *

start_system = True
while start_system :

    print("*"*50)
    print("전화번호 관리 프로그램")
    print("*"*50)

    status = True
    person_list = get_list()

    while status :

            print("1.리스트 2.등록 3.삭제 4.검색 5.종료")
            print("-"*38)
            menu = int(input(">메뉴번호:"))

            match menu :
                 
                case 1 :
                    print("<1.리스트>")
                    read_list (person_list)

                case 2: #등록 
                    print("<2.등록>")
                    person = []
                    person[0] = input("이름> ")
                    person[1] = input("휴대전화> ")
                    person[2] = input("회사전화> ")
                    insert_list (person_list, person)

                case 3: #삭제
                    print("<3.삭제>")
                    delete_list (person_list)

                case 4: #검색
                    pass

                    # index 찾기

                    # print(b.index(1000))

                case 5: #종료
                    print("*"*50)
                    print("감사합니다")
                    print("*"*50)
                    start_system = False
                    status = False
                
                      






