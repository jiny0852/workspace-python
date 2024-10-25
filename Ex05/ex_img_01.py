import os  # os 모듈을 사용해서 환경변수에 접근
from openai import OpenAI

# 컴퓨터의 한경변수의 키 값을 읽어 옴
openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=openai_api_key)

prompt_txt = '''
"green iced melon soda with whip cream and red cheery on top"
애니메이션 풍으로 만들어줘
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







