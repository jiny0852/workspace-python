# 25 MB 넘으면 잘라서 하는 방법도
import os
from openai import OpenAI

openai_api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key = openai_api_key)


audio_file= open("C:\\javaStudy\\workspace-python\\Ex05\\poem.mp3", "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)
print(transcription.text)





