# Setting Up Your Streamlit App to Use Gemini
 
## 1. Get a free API key
 
1. Go to **https://aistudio.google.com/apikey**
2. Sign in and click **Create API key**.
3. Copy it.
Keep it private. Never put it in your code or your repo.
 
## 2. Add the key to Streamlit
 
**Manage app → Settings → Secrets**, and paste:
 
```toml
MyGeminiKey = "AIza..."
```
 
Your code reads it with:
 
```python
client = genai.Client(api_key=st.secrets["MyGeminiKey"])
```
 
## 3. Delete three files from your repo
 
```
pyproject.toml
uv.lock
.python-version
```
 
## 4. Create `requirements.txt`
 
```
streamlit
google-genai
```
 
Add other package names as needed.
 
 
## 5. Reboot
 
**Manage app → ⋮ → Reboot app**, then watch the build log.


## Llama version (no API key)

`llama_demo/streamlit_app_llama.py` is the same app, but the model runs **inside the app**: Llama 3.2 1B, compressed to 4 bits (about 0.8 GB), downloaded from Hugging Face the first time the app starts.

To deploy it, set **Main file path** to `llama_demo/streamlit_app_llama.py`. No secrets are needed. Community Cloud uses the `requirements.txt` inside `llama_demo/`, not the one at the top of the repo. The first visitor waits about a minute while the model downloads.
