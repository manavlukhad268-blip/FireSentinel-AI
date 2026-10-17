
# FireSentinel AI - Voice Threat & Scam Detection
import speech_recognition as sr
from gtts import gTTS

print("=== FireSentinel AI Starting ===")

THREAT_KEYWORDS = ["otp", "bank", "credit card", "pin", "lottery", "urgent", "police", "blocked"]

def analyze_audio_text(text):
    text_lower = text.lower()
    detected_threats = [word for word in THREAT_KEYWORDS if word in text_lower]
    if detected_threats:
        return f"ALERT: Potential scam detected! Keywords: {', '.join(detected_threats)}"
    return "SAFE: No threat detected."

sample_input = "Your bank account is blocked, share your OTP immediately."
result = analyze_audio_text(sample_input)
print(result)

tts = gTTS(text=result, lang='en')
tts.save("warning.mp3")
