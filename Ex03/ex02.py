
#0.import
import mysql.connector
from mysql.connector import Error # 관련 에러 싹 모다 놓음 얘 갔다 쓰면됨


host='localhost' # 호스트
user='phonebook' # 사용자명
password='phonebook' # 비밀번호
database='phonebook_db' # 데이터베이스명
port=3306




try :

    #1.연결/컨넥션 얻기
    try :
        
        conn = mysql.connector.connect(

            host=host, # 호스트
            user=user, # 사용자명
            password=password, # 비밀번호
            database=database, # 데이터베이스명
            port=port

            # host='localhost', # 호스트
            # user='phonebook', # 사용자명
            # password='phonebook', # 비밀번호
            # database='phonebook_db', # 데이터베이스명
            # port=3306

        )
        print("연결 성공")

    except Error as err :
        print(f"연결 오류: {err}")



    #2.커서생성
    cursor = conn.cursor()

    #3.SQL문준비 / 바인딩 / 실행  #insert문, update문, delete문

    #--SQL문
    query = """

        select  person_id,
                name,
                hp,
                company
        from person

    """
    print(query)

    #--바인딩(튜플)

    #--실행
    cursor.execute(query)
    resultset = cursor.fetchall()

    #4.결과처리 리스트 [(튜플), (튜플), (튜플)] -> 리스트[{딕셔너리}, 딕셔너리}, 딕셔너리}]
    # print(resultset[0][1])

    person_list = []
    for row in resultset:

        person_vo = {
            "person_id": row[0],        #person_id
            "name": row[1],             #name
            "hp": row[2],               #hp
            "comp[any]": row[3]         #company
        }
        person_list.append(person_vo)

    print(person_list)
    print(person_list[0]["name"])


except Error as e:

    print(f"데이터베이스 오류: {e}")


finally:
    #5.자원정리
    if cursor is not None:

        cursor.close()

    if conn is not None :

        conn.close()










