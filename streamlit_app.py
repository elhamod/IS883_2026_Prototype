import streamlit as st
from google import genai
from google.genai import types
from google.colab import userdata

### Load your API Key
client = genai.Client(api_key=st.secrets['MyGeminiKey'])

MODEL = "gemini-3.1-flash-lite"


# st.title("🎈 My new app")
# st.write(
#     "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
# )
st.write("Press the button to say hello")
if st.button("Press me!"):
    st.write(client.models.generate_content(model=MODEL, contents="Say hello in five words.").text)

