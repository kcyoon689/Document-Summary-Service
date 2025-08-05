# 📄 SmartForm Assistant

**SmartForm Service** is a Streamlit-based web application that leverages Upstage’s Solar API to automatically perform **summarization**, **classification**, **response generation**, **urgency detection**, and **question answering** for text-based civil complaints.

---

## 🚀 Key Features

- 📋 **Display & Analyze Complaint Text**
- 🧠 **Document Summarization**: Concisely summarizes lengthy complaint content
- 🏷️ **Complaint Classification**: Automatically categorizes complaints (e.g., Road, Environment, Noise, Safety, Others)
- ✍️ **Automated Response Generation**: Generates polite and concise responses to the complaint
- 📢 **Urgency Detection**: Identifies urgent complaints based on keywords such as “damage,” “accident,” or “danger”
- 💬 **Question Answering**: Answers user queries based on complaint content

---

## 🖼️ App Structure

```text
📄 SmartForm Assistant
├─ 🗒️ Complaint Text Input
├─ 📝 Summary Output
├─ 🏷️ Complaint Classification
├─ 📬 Automated Response
├─ 💬 Document-based Q&A
├─ 📢 Urgency Detection
```

---

## 🛠️ Installation

1. Requires Python 3.10 or higher.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Replace the `API_KEY` variable in `summarizer.py`, `classifier.py`, and `response_generator.py` with your key from [Upstage Console](https://console.upstage.ai/).

---

## ▶ Run the App

```bash
streamlit run app.py
```

> After launching, visit `http://localhost:8501` or the address shown in your terminal.

---

## 📁 Directory Structure

```
smartform_app_final/
├── app.py                    # Streamlit main application
│
├── /api
│   ├── summarizer.py            # Summarization & QA logic
│   ├── classifier.py            # Complaint classification
│   ├── response_generator.py    # Automated response generation
│   └── function_caller.py       # Urgency detection logic
│
├── /sample
│   └── complaint_sample.txt     # Sample complaint text
│
├── /utils
│   └── file_utils.py            # File reading utility
│
└── requirements.txt         # Dependency list
```

---

## 🧠 Technologies Used

- [Streamlit](https://streamlit.io/)
- [Upstage Solar API](https://console.upstage.ai/)
- Python (`requests`, `json`)

---

## 📌 Future Improvements

- [ ] Add PDF upload support
- [ ] Integrate image-based OCR complaint intake
- [ ] Admin dashboard
- [ ] Real-time alert system (email, Slack)
