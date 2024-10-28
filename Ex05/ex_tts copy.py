from pathlib import Path
import os
import openai

openai_api_key = os.getenv("OPENAI_API_KEY")

openai.api_key = 'openai_api_key'



response = openai.Audio.create(
    # model="tts-1",
    # voice="alloy",
    
    model="text-to-speech",
    text="안녕 오점메좀 추천해줘",
    voice="desired_voice_model",  # 원하는 음성 모델을 입력
    speed=1.0,  # 속도 조정 (1.0이 기본)
    pitch=0.0,   # 피치 조정 (0.0이 기본)
    response_format="mp3"
)


with open('output.mp3', 'wb') as f:
    f.write(response['audio'])













