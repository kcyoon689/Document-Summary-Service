import requests
import json

API_KEY = "up_...."
# URL = "https://api.upstage.ai/v1/solar"
URL = "https://api.upstage.ai/v1/solar/chat/completions"


def classify_issue(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "solar-pro2",
        "messages": [
            {"role": "system", "content": "당신은 민원 유형 분류기입니다. [도로, 환경, 소음, 안전, 기타] 중 하나로만 대답하세요."},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content'].strip()
