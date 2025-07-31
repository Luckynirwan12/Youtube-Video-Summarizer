# 🎥 YouTube Video Summarizer
A simple and effective Streamlit web app that generates a detailed summary of any YouTube video using its transcript and Google Gemini (Generative AI).

---

### ✨ Features
- 🔗 Paste YouTube Video URL in the sidebar

- 📄 Generates a concise summary in bullet points using Google Gemini

- 🖼️ Displays the video thumbnail

- 📥 Option to download the summary as a PDF

- 🧠 Utilizes youtube_transcript_api and Gemini for intelligent summarization

---

### 🚀 Demo
| 📌 Paste the YouTube link ➝ Click Get Detailed Notes ➝ View summary ➝ Download PDF

---

### 🛠️ Tech Stack
- Streamlit

- Google Generative AI (Gemini)

- YouTube Transcript API

- FPDF

---

### 📦 Installation
1. Clone the repo

       git clone https://github.com/yourusername/youtube-video-summarizer.git
       cd youtube-video-summarizer

3. Install dependencies

       pip install -r requirements.txt

4. Set up environment variable

Create a .env file in the root directory and add your Gemini API key:

    GOOGLE_API_KEY=your_google_api_key

---

### ▶️ Run the App

    streamlit run app.py

---

### 🗂️ Project Structure

youtube-video-summarizer/

├── .venv/                   # Virtual environment

├── .env                     # API keys (Not committed to GitHub)

├── app.py                   # Main Streamlit app

├── requirements.txt         # Python dependencies

---
       
