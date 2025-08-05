def analyze_and_alert(summary_text):
    if "파손" in summary_text or "사고" in summary_text or "위험" in summary_text:
        return {
            "status": "sent",
            "category": "도로",
            "urgency": "긴급",
            "summary": summary_text
        }
    return {
        "status": "not urgent",
        "summary": summary_text
    }
