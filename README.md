
# FireSentinel AI 🛡️🔥
AI-powered voice threat & scam detection app designed for Fire TV / Vega OS (16:9 widescreen 10-foot UI).

## 🚀 Overview
FireSentinel AI protects users from voice scams, fraudulent calls, and security threats by analyzing audio in real-time and generating instant alerts on smart TV screens.

## 🛠️ Tech Stack (100% Open-Source & Free)
- **Speech Processing & AI Brain:** Python, SpeechRecognition / Whisper, Hugging Face open-source modules.
- **Audio Output:** gTTS (Google Text-to-Speech).
- **Backend Database:** Supabase.

## ☁️ Note on AWS Integration & Architecture
- **Design Intent:** The project architecture is fully compatible with AWS services (such as Amazon Bedrock and Amazon Transcribe) using the Python `boto3` SDK.
- **Implementation Status:** Live production AWS integration has been intentionally omitted and replaced with 100% free, open-source Python libraries. 
- **Reason:** Creating a live cloud account required credit/debit card details and billing setups, which are restricted as a student participant. To ensure zero billing risk and maintain a completely free architecture, the core logic relies on verified open-source components while keeping the AWS-ready design documented for scalability.

## 📄 License
This project is licensed under the MIT License.
