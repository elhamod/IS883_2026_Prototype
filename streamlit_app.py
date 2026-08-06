import streamlit as st
from google import genai
from google.genai import types
from google.colab import userdata

### Load your API Key
gemini_api_key = st.secrets['MyGeminiKey']# Info: https://docs.streamlit.io/develop/api-reference/connections/st.secrets
client = genai.Client(api_key=gemini_api_key)

MODEL = "gemini-3.1-flash-lite"

st.write("Press the button to say hello")
if st.button("Press me!"):
    st.write(client.models.generate_content(model=MODEL, contents="Say hello in five words.").text)

