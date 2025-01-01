import streamlit as st
from browser_transcribe import browser_transcribe

# renders the browser_transcribe component
transcribe = browser_transcribe()

# displays the transcribed text
st.markdown(transcribe)


