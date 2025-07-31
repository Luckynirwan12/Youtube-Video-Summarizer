import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from youtube_transcript_api import YouTubeTranscriptApi
from fpdf import FPDF
import io

# Load environment variable
load_dotenv()

# Setup your Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Prompt for the LLM
prompt = "You are a Youtube Video Summarizer. You will be taking the transcript text and summarizing the entire video and providing the important summary in points within 250 words. Please provide the summary of the text given here:"

# Getting the Transcript data fron YT videos
def extract_transcript_detail(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1]
        ytt_api = YouTubeTranscriptApi()
        transcript = ytt_api.fetch(video_id)
        text = " ".join([entry.text for entry in transcript])
        return text

    except Exception as e:
        st.error(f"Error fetching transcript: {e}")
        return None

# Getting the Summary based on Prompt from Google Gemini
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel()
    response = model.generate_content(prompt+transcript_text)
    return response.text


def create_pdf(summary_text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Split text into lines that fit the page
    for line in summary_text.split('\n'):
        pdf.multi_cell(0, 10, line)

    # Return as byte stream
    pdf_output = pdf.output(dest='S').encode('latin1')  # 'S' returns as string
    return io.BytesIO(pdf_output)

# Streamlit app
st.set_page_config(page_title="YouTube Video Summarizer 🎬", layout="centered")
st.title("🎥 YouTube Video Summarizer")

# Sidebar input
st.sidebar.header("🔗 Upload the URL :")
st.sidebar.markdown("*Just paste the YouTube video URL that you want to summarize and then click the button below to get the summary.*")
video_url = st.sidebar.text_input("📎 Enter YouTube Video URL")
get_summary = st.sidebar.button("Get Detailed Notes")

if not (get_summary and video_url):
    st.success("_📌 To begin, paste a YouTube video link in the sidebar and click 'Get Detailed Notes'._")

if get_summary and video_url:
    video_id = video_url.split("v=")[1]
    # Show thumbnail
    st.subheader("🖼️ Thumbnail:")
    st.image(f"https://img.youtube.com/vi/{video_id}/0.jpg", use_container_width=True)

    with st.spinner("⏳ Processing... Fetching transcript and generating summary..."):
        transcript_text = extract_transcript_detail(video_url)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.header("📄 Detailed Summary:")
            st.write(summary)

            # PDF download button in sidebar
            pdf_file = create_pdf(summary)
            st.sidebar.header("📥 Download the Summary :")
            st.sidebar.markdown("*You can download the summary of the YouTube video by clicking the button below.*")
            st.sidebar.download_button(
                label="⬇️ Download as PDF",
                data=pdf_file,
                file_name="youtube_summary.pdf",
                mime="application/pdf"
            )










