print("파이썬")

#0.import
import mysql.connector
from mysql.connector import Error # 관련 에러 싹 모다 놓음 얘 갔다 쓰면됨


try :

    print("파이썬222")

    #1.연결/컨넥션 얻기
    try :
        
        conn = mysql.connector.connect(

            host='localhost', # 호스트
            user='phonebook', # 사용자명
            password='phonebook', # 비밀번호
            database='phonebook_db', # 데이터베이스명
            port=3306

        )
        print("연결 성공")

    except Error as err :
        print(f"연결 오류: {err}")



    print("파이썬333")
    #2.커서생성
    cursor = conn.cursor()
    print("파이썬444")

    #3.SQL문준비 / 바인딩 / 실행  #insert문, update문, delete문

    #--SQL문
    query = """

        insert into person
        values(null, %s, %s, %s)

    """
    print(query)

    #--바인딩(튜플)
    data = ("차은우", "010-999-9999", "02-9999-9999")

    print(query, data)

    #--실행
    cursor.execute(query, data) #실행(임시) -> 롤백 리롤 대기중  //임시반영
    conn.commit() #반영(실제) 리턴값은 없다                      //최종반영


    #4.결과처리
    print(f'{cursor.rowcount}개 저장')




except Error as e:

    print(f"데이터베이스 오류: {e}")


finally:
    #5.자원정리
    # conn.close()
    # cursor.close()

    if cursor is not None:

        cursor.close()

    if conn is not None :

        conn.close()










