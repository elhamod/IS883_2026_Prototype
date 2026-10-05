import streamlit as st
from google import genai
from google.genai import types

# Load your API Key
try:
    gemini_api_key = st.secrets["MyGeminiKey"]
except (KeyError, FileNotFoundError):
    st.error("No Gemini key found.")
    st.stop()

client = genai.Client(api_key=gemini_api_key)

MODEL = "gemini-3.1-flash-lite"

# Choose response style
mood = st.radio(
    "How should Gemini respond?",
    ["Happy", "Sad"],
)

st.write("Press the button to ask Gemini")

if st.button("Press me!"):
    response = client.models.generate_content(
        model=MODEL,
        contents=f"""
        Write a haiku.
        Respond in a {mood.lower()} tone.
        """
    )
    
    st.write(response.text)
