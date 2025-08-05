import requests
import json

API_KEY = "up_...."
# URL = "https://api.upstage.ai/v1/solar"
URL = "https://api.upstage.ai/v1/solar/chat/completions"

def generate_response(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "solar-pro2",
        "messages": [
            {"role": "system", "content": "당신은 민원 응답 작성자입니다. 정중하고 간결한 응답을 작성하세요."},
            {"role": "user", "content": text}
        ]
    }
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content'].strip()
