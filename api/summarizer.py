import requests
import json

API_KEY = "up_...."
# URL = "https://api.upstage.ai/v1/solar"
URL = "https://api.upstage.ai/v1/solar/chat/completions"


def summarize_doc(text):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "solar-pro2",
        "messages": [
            {"role": "system", "content": "당신은 문서 요약 도우미입니다."},
            {"role": "user", "content": f"다음 문서를 요약해줘:\n{text}" }
        ]
    }
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    # print("=== RESPONSE TEXT ===")
    # print(response.text)
    print("=== RESPONSE STATUS ===", response.status_code)
    print("=== RESPONSE TEXT ===", response.text)
    return response.json()['choices'][0]['message']['content']

def ask_question(context, question):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "solar-pro2",
        "messages": [
            {"role": "system", "content": f"문서 내용:\n{context}"},
            {"role": "user", "content": question}
        ]
    }
    response = requests.post(URL, headers=headers, data=json.dumps(data))
    return response.json()['choices'][0]['message']['content']
