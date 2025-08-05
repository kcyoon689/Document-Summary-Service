import streamlit as st
from api.summarizer import summarize_doc, ask_question
from api.function_caller import analyze_and_alert
from api.classifier import classify_issue
from api.response_generator import generate_response
from utils.file_utils import read_txt_file

st.set_page_config(page_title="SmartForm 도우미", layout="wide")
st.title("📄 SmartForm 도우미 - 샘플 민원 자동 분석")

sample_path = "sample/complaint_sample.txt"
raw_text = read_txt_file(sample_path)

st.subheader("🗒️ 샘플 민원 내용")
st.text_area("텍스트", raw_text, height=250)

with st.spinner("🧠 요약 중..."):
    summary = summarize_doc(raw_text)
st.subheader("📝 요약 결과")
st.write(summary)

with st.spinner("📂 민원 유형 분류 중..."):
    issue_type = classify_issue(summary)
st.subheader("🏷️ 민원 유형")
st.write(f"예상 분류: **{issue_type}**")

with st.spinner("✍️ 민원 응답 생성 중..."):
    response_text = generate_response(raw_text)
st.subheader("📬 자동 응답")
st.write(response_text)

st.subheader("💬 문서 관련 질문")
user_question = st.text_input("질문을 입력하세요:")
if user_question:
    with st.spinner("답변 생성 중..."):
        answer = ask_question(summary, user_question)
    st.success(f"🗨️ 답변: {answer}")

with st.spinner("⚠️ 긴급 민원 여부 분석 중..."):
    alert_result = analyze_and_alert(summary)
    st.subheader("📢 자동 알림 결과")
    st.json(alert_result)
