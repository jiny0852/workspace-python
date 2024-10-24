#1. 최소버전+토큰값
#2. 이전 내용 기억하기
#3. 사용자 질문 입력하기
#4. 반복해서 질문 입력하기, 종료가능
#5. 대화 내용 누적 -> 토큰(비용)을 많이 사용해야한다
#6. 배경(1)+질+답(5*2) --> 11개만 보관  우리 사이트의 정보가 없다
#7. system 사이트 정보 추가
#8. 사이트 정보 함수로 호출하기



import os  # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI

import chat_dao




# 컴퓨터의 한경변수의 키 값을 읽어 옴
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

#메세지 갯수
num = 7

# system 프롬프트
prompt_txt = chat_dao.get_data()

message_history = [
    {"role": "system","content": prompt_txt,},
]


# 사용자로부터 질문입력 받기
print("*******************************")
print("***반갑습니다. 질문을 입력해주세요***\n")
print("*******************************")


while True : 

    # if len(message_history) >= 11 :
    #     print("*******************************")
    #     print("질문 갯수가 초과되었습니다(5)")
    #     break
    # else :

        question = input("(사용자)")


        if (question == "\q") :
            break


        else :

            # 질문 추가
            message_history.append({"role": "user", "content": question})
            

            response = client.chat.completions.create(
                model="gpt-3.5-turbo-0125",
                messages=message_history,
                temperature=1,                    # 엉뚱한 단어
                max_tokens=2048,
                top_p=1,                          # 다양한 문장 형식 1~5형식
                frequency_penalty=0,              # 중복단어 제한 
                presence_penalty=0,               # 다른 주제까지 확장
                response_format={"type": "text"},
            )

            print(f"[챗_GPT]{response.choices[0].message.content}")
            message_history.append({"role": "assistant", "content": response.choices[0].message.content})





            # 총 num개의 데이터만 유지 최근꺼만
            if len(message_history) > num :
                message_history = [message_history[0]] + message_history[-4:]
                print(message_history)







print("*******************************")
print("***종료합니다><***\n")
print("*******************************")







