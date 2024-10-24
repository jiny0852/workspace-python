
from phonedao import *

start_system = True
while start_system :

    print("*"*50)
    str_start = "전화번호 관리 프로그램"
    print(str_start.center(38))
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

                    insert_list (person_list)


                case 3: #삭제
                    print("<3.삭제>")
                    delete_list (person_list)


                case 4: #검색
                    print("<4.검색>")
                    str_search = input(">이름: ")
                    search_list(person_list, str_search)


                case 5: #종료
                    save_list(person_list)

                    print("*"*50)
                    str_end = "감사합니다"
                    print(str_end.center(38))
                    print("*"*50)

                    start_system = False
                    status = False

                case _:
                      print("다시 입력해주세요")
                
                      






