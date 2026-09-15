import threading

import streamlit as st
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

### Load a small Llama that runs inside the app itself: no API key, no secrets.
# Llama 3.2 1B, compressed to 4 bits per weight (~0.8 GB), so it fits in Community Cloud's memory limit.
MODEL_REPO = "bartowski/Llama-3.2-1B-Instruct-GGUF"
MODEL_FILE = "Llama-3.2-1B-Instruct-Q4_K_M.gguf"

@st.cache_resource(show_spinner="Downloading Llama 3.2 1B (about 800 MB). Only the first visitor waits for this...")
def load_model():
    model_path = hf_hub_download(repo_id=MODEL_REPO, filename=MODEL_FILE)
    llm = Llama(model_path=model_path, n_ctx=1024, n_threads=2, verbose=False)
    return llm, threading.Lock()  # one model shared by every visitor, answering one request at a time

llm, lock = load_model()

st.write("Press the button to say hello")
if st.button("Press me!"):
    with lock, st.spinner("Llama is thinking on this app's CPU..."):
        reply = llm.create_chat_completion(
            messages=[{"role": "user", "content": "Say hello in five words."}],
            max_tokens=32,
        )
    st.write(reply["choices"][0]["message"]["content"])
