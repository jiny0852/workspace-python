from pathlib import Path
import os
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)

text = '''
서시
윤동주

죽는 날까지 하늘을 우러러
한 점 부끄럼이 없기를,
잎새에 이는 바람에도
나는 괴로워했다.
별을 노래하는 마음으로
모든 죽어 가는 것을 사랑해야지
그리고 나한테 주어진 길을
걸어가야겠다.

오늘 밤에도 별이 바람에 스치운다.

'''

#speech_file_path = Path(__file__).parent / "speech.mp3"
response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=text,
    response_format="mp3",
    speed=1.5
)

# response.stream_to_file(speech_file_path)

speech_file_path = "C:\\javaStudy\\workspace-python\\Ex05\\tts.mp3"


# file = open(speech_file_path, "wb") //아래의 역할 하는것 
with open(speech_file_path, "wb") as file :   
    file.write(response.content) 
    #알아서 file.close() <-- with문법
