
import os
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)

prompt_txt = """
    #persona
    당신은 대한민국의 행복한 가정에서 자란 시를 좋아하는 10살 아이입니다

    #tone
    맑고 밝고 명랑한 아이의 말투를 사용합니다

    #example
    비슷한 내용으로 작성합니다
    1. 나비와 꽃

    나비가 날아와
    꽃 위에 앉았네.
    향기 가득한 봄날,
    우리 함께 놀자네.

    2. 비 오는 날

    빗방울 떨어져
    탁탁탁 소리 나.
    우산 펴고 나가면
    신나는 물장구야.

    3. 나무 그늘

    푸른 나무 아래
    그늘이 시원해.
    바람이 살랑살랑,
    우린 그네 타며.

    4. 별빛이 반짝

    밤하늘 별빛이
    하나 둘 셋, 반짝.
    소원을 빌어볼까,
    꿈이 이루어지길!

    #task 
    동시를 지어주세요

    #format
    100글자 이내로 작성합니다
"""

message_history = [
    {"role": "system","content": prompt_txt,},
]


print("*******************************")
print("******주제를 입력해주세요******\n")



question = input("주제: ")


#주제 추가
message_history.append({"role": "user", "content": question})

response = client.chat.completions.create(
    model="gpt-3.5-turbo-0125",
    messages=message_history,
    temperature=1,                    
    max_tokens=2048,
    top_p=1,                          
    frequency_penalty=0,              
    presence_penalty=0,               
    response_format={"type": "text"},
)

message_history.append({"role": "assistant", "content": response.choices[0].message.content})
result = response.choices[0].message.content
print(result)

        

response = client.audio.speech.create(
    model="tts-1",
    voice="nova",
    input=result,
    response_format="mp3",
    speed=1.5
)


speech_file_path = "C:\\javastudy\\upload\\poem.mp3"

with open(speech_file_path, "wb") as file :   
    file.write(response.content) 


print()
print("**********종료합니다**********\n")