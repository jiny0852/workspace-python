
# 함수로 호출하던지 파일로 만들어서 파일을 읽게 하던지


def get_data():
    prompt_txt = '''






    '''
    return prompt_txt



#persona

#example

#context

#task

#format

#tone



py -3.11 -m venv ex01_venv


with open('C:/javaStudy/workspace_py/Ex05/terms_and_conditions.txt', 'r', encoding='utf-8') as file:
    terms = file.read()
#system 프롬프트
prompt_txt = f"""
                #context
                {terms}
                #persona
                -약관에 없는 내용을 물어보는 경우 고객센터 02-123-4567로 연락하도록 안내
                -너는 10년차 베테랑 상담원이야
                #tone
                -친절하고 존댓말을 사용
            """

@함민규 형님 아까 말했던거에용 파일로 저장하는 방법



#토큰수 확인
q_token = response.usage.prompt_tokens      #질문토큰수
a_token = response.usage.completion_tokens    #응답토큰수
total_token = response.usage.total_tokens    # 전체 토큰 수
print(f"질문:{q_token} 응답:{a_token} 전체:{total_token}")

# GPT-3.5 터보 모델의 요금 (1,000 토큰당 $0.002)
gpt_35_turbo_cost_per_1k_tokens = 0.002  

# GPT-3.5 터보 모델의 총 비용 계산
cost_gpt_35_turbo = total_token / 1000 * gpt_35_turbo_cost_per_1k_tokens
print(f"GPT-3.5 터보 사용 예상 비용: ${cost_gpt_35_turbo:.6f}")