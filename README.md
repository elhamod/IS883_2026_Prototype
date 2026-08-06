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
