import os  # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI

import uuid
import requests

# 컴퓨터의 한경변수의 키 값을 읽어 옴
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

prompt_txt = '''
"iced melon soda"
실제 사진 처럼 만들어줘
'''

response = client.images.generate(
    model="dall-e-3",
    prompt=prompt_txt,
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print(image_url)


#다운로드 받을 경로
download_path = "C:\\javaStudy\\upload_py"

# 파일이름 생성
file_name = str(uuid.uuid4())+".png"

#이미지 다운로드
response = requests.get(image_url)
if response.status_code == 200 :  #200은 성공 주소 유효
    file_path = os.path.join(download_path, file_name)
    with open(file_path, "wb") as file:
        file.write(response.content)

    print("다운로드 완료")

else :
    print("url 오류")




