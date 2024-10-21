

file_path = "C:\\javaStudy\\workspace-python\\phonefile\\PhoneDB.txt"



# 파일 데이터 뽑아서 리스트로 보내기 

def get_list() :

    person_list = []

    with open(file_path, 'r', encoding="utf-8") as file:
        
        data = file.read()
        persons = data.split("\n")

        #print(persons)
        # print("===============")

        i = 0
        for person in persons:
                person_list.append(persons[i].split(","))
                i += 1

     #    print("person_list")
     #    print(person_list)
     #    print(person_list[1][1])
    
    return person_list


# get_list()


def read_list(person_list) :
     i = 0
     for person in person_list :
          print(i+1, person_list[i][0], person_list[i][1], person_list[i][2])
          i += 1

     print()


# 리스트 등록하기
def insert_list (person_list, person) :

     


     print(person)
     
     person_list.append(person)
     print(person_list)

     return(person_list)


# 리스트 삭제하기
def delete_list (person_list) :
     person_list.remove(person_list[(int(input("삭제번호를 입력하세요> "))-1)])

     return(person_list)

# 리스트 검색하기
def search_list () :
     pass






