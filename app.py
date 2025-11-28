# app.py
import streamlit as st
import os, random, time
from questions import QUESTION_BANK, ROLE_TO_FIELDS, ALL_FIELDS
from analysis import compute_scores
from voice_interview import transcribe_audio_file
from db import init_db, save_interview
from pdf_report import create_pdf

st.set_page_config(page_title="VoiceHire AI", page_icon="🎤", layout="centered")
st.title("🎤 VoiceHire AI — Multi-Domain AI Interviewer")

init_db()

# Sidebar
st.sidebar.header("Settings")
field = st.sidebar.selectbox("Field", ["Auto-detect"] + sorted(ALL_FIELDS))
role = st.sidebar.text_input("Role (optional)")
name = st.sidebar.text_input("Your Name")

def get_questions(field, role):
    selected = []

    if field != "Auto-detect":
        selected.append(field)

    if role:
        r = role.lower()
        for key, fields in ROLE_TO_FIELDS.items():
            if key in r:
                selected += fields

    if not selected:
        selected = ["general"]

    questions = []
    for f in selected:
        questions += QUESTION_BANK.get(f, [])

    questions += QUESTION_BANK["general"]

    return list(dict.fromkeys(questions))  

questions_list = get_questions(field, role)

st.subheader("Interview Question")
q_index = st.number_input("Select Question Number", 1, len(questions_list), 1)

if st.button("Random Question"):
    q_index = random.randint(1, len(questions_list))

question = questions_list[q_index - 1]
st.write(f"**Question:** {question}")

answer_mode = st.radio("Answer Method:", ["Type Answer", "Upload Audio"])

transcript = ""
duration = 0

if answer_mode == "Type Answer":
    transcript = st.text_area("Type your answer:")
else:
    audio_file = st.file_uploader("Upload Audio (mp3 or wav)", type=["wav","mp3"])
    if audio_file:
        with open("temp_audio", "wb") as f:
            f.write(audio_file.read())

        st.info("Transcribing...")
        try:
            start = time.time()
            transcript = transcribe_audio_file("temp_audio")
            duration = time.time() - start
            st.success("Transcription complete.")
        except:
            st.error("Transcription failed. Please type your answer.")
        try:
            os.remove("temp_audio")
        except:
            pass

if transcript:
    st.subheader("Transcript")
    st.write(transcript)

if st.button("Analyze"):
    if not transcript:
        st.error("No answer provided.")
    else:
        score, breakdown = compute_scores(transcript, duration)
        st.metric("Interview Score", f"{score}/100")
        st.json(breakdown)

        if st.checkbox("Save Result"):
            save_interview(name or "Unknown", field, question, transcript, score, breakdown)
            st.success("Saved successfully.")

        if st.button("Download PDF Report"):
            pdf = create_pdf(name or "Candidate", question, transcript, breakdown)
            st.download_button("Download", data=pdf, file_name="Interview_Report.pdf")
