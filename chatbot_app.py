import streamlit as st
from google import genai
from google.genai import types

### Load your API Key
try:
    gemini_api_key = st.secrets['MyGeminiKey']# Info: https://docs.streamlit.io/develop/api-reference/connections/st.secrets
except (KeyError, FileNotFoundError):
    st.error("No Gemini key found. Add `MyGeminiKey` under **Manage app → ⋮ → Settings → Secrets**, then refresh this page.")
    st.stop()
client = genai.Client(api_key=gemini_api_key)

MODEL = "gemini-3.1-flash-lite"

st.title("Minimal Gemini Chatbot")

### Generation parameters
temperature = st.sidebar.slider("Temperature", 0.0, 2.0, 1.0)
max_tokens = st.sidebar.slider("Max output tokens", 50, 2000, 500)

### Memory: Streamlit reruns this script on every interaction, so the chat history lives in st.session_state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show the conversation so far
for message in st.session_state.messages:
    avatar = "user" if message["role"] == "user" else "assistant"
    st.chat_message(avatar).write(message["parts"][0]["text"])

if prompt := st.chat_input("Say something"):
    st.session_state.messages.append({"role": "user", "parts": [{"text": prompt}]})
    st.chat_message("user").write(prompt)

    # Send the WHOLE history every turn -- the model itself remembers nothing between calls
    response = client.models.generate_content(
        model=MODEL,
        contents=st.session_state.messages,
        config=types.GenerateContentConfig(temperature=temperature, max_output_tokens=max_tokens),
    )

    st.session_state.messages.append({"role": "model", "parts": [{"text": response.text}]})
    st.chat_message("assistant").write(response.text)
