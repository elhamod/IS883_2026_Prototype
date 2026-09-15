import threading

import streamlit as st
from llama_cpp import Llama

### Load a small Llama that runs inside the app itself: no API key, no secrets.
# Llama 3.2 1B, compressed to 4 bits per weight (~0.8 GB), so it fits in Community Cloud's memory limit.
@st.cache_resource(show_spinner="Downloading Llama 3.2 1B (about 800 MB). Only the first visitor waits for this...")
def load_model():
    llm = Llama.from_pretrained(repo_id="bartowski/Llama-3.2-1B-Instruct-GGUF", filename="*Q4_K_M.gguf", n_threads=2)
    return llm, threading.Lock()  # one model shared by every visitor, answering one request at a time

llm, lock = load_model()

st.write("Press the button to say hello")
if st.button("Press me!"):
    with st.spinner("Llama is thinking on this app's CPU..."), lock:
        reply = llm.create_chat_completion(
            messages=[{"role": "user", "content": "Say hello in five words."}],
            max_tokens=32,
        )
    st.write(reply["choices"][0]["message"]["content"])
