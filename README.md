# IS883 Streamlit Prototypes

This repository contains three separate Streamlit apps. Streamlit Community Cloud runs **one file per app**, and you pick that file when you deploy.

| App | Main file path | What it does | Needs the Gemini key? |
| --- | --- | --- | --- |
| Hello button | `streamlit_app.py` | Asks Gemini to say hello when you press a button | Yes |
| Chatbot | `chatbot_app.py` | A Gemini chat that remembers the conversation | Yes |
| Llama hello button | `llama_demo/streamlit_app_llama.py` | The same hello button, but the model (Llama 3.2 1B, about 0.8 GB) runs **inside the app** | No |

---

## 1. Get a free Gemini API key (Gemini apps only)

1. Go to **https://aistudio.google.com/apikey**
2. Sign in and click **Create API key**.
3. Copy it.

Keep it private. **Never put it in your code or your repo.** The apps read it from Streamlit's secrets:

```python
client = genai.Client(api_key=st.secrets["MyGeminiKey"])
```

## 2. Deploy an app

Every app gets its own web address, so you can keep all three running side by side from the same repository. For **each** app you want:

1. Go to **[share.streamlit.io](https://share.streamlit.io)** and click **Create app** (upper-right).
2. Choose **Yup, I have an app**.
3. Fill in:
   - **Repository:** your copy of this repository
   - **Branch:** `main`
   - **Main file path:** copy it from the table above, e.g. `chatbot_app.py`
   - **App URL:** optional, pick a name you will remember
4. Click **Advanced settings**:
   - For the two **Gemini** apps, paste your key into **Secrets**:
     ```toml
     MyGeminiKey = "AIza..."
     ```
   - For the **Llama** app, leave Secrets empty.
   - Click **Save**.
5. Click **Deploy** and watch the build log.

Secrets belong to **one app**, not to the repository, so each Gemini app needs its own copy of the key. To add or change a secret later: **Manage app → ⋮ → Settings → Secrets**.

## 3. Switch an existing app to a different file

Once an app is deployed, you **cannot change its main file** from its settings. Either deploy another app (step 2), or:

1. Open your app, click **Manage app** (lower-right), then **⋮ → Delete app**, and confirm.
2. Deploy again (step 2) with the **new** main file path.
   - Your old app URL is freed right away, so you can type the same one again.
   - Re-enter your secrets if the new app uses Gemini.

## 4. Packages: nothing to edit

Community Cloud looks for `requirements.txt` **in the same folder as the main file first**, then at the top of the repository:

- `streamlit_app.py` and `chatbot_app.py` use the top-level `requirements.txt`.
- `llama_demo/streamlit_app_llama.py` uses `llama_demo/requirements.txt`.

This is why the Llama app lives in its own folder. **Don't move or rename its files**, or it will pick up the wrong package list. If you add a package to a Gemini app, add its name to the top-level `requirements.txt`.

---

## Troubleshooting

| What you see | What to do |
| --- | --- |
| `KeyError: 'MyGeminiKey'` or a message about missing secrets | The app's secret is missing or misspelled. **Manage app → ⋮ → Settings → Secrets**. |
| `ModuleNotFoundError: No module named 'llama_cpp'` | The Llama file was moved out of `llama_demo/`, so the wrong `requirements.txt` was used. |
| Packages you listed in `requirements.txt` are not installed | Delete any `uv.lock`, `pyproject.toml`, or `.python-version` in your repo. Community Cloud uses those *instead of* `requirements.txt`. |
| The Llama app shows "Downloading Llama 3.2 1B…" for a minute or more | Normal. The model downloads from Hugging Face the first time the app starts, and again after it restarts. |
| The Llama app is slow to answer | Normal. It runs on the app's small CPU, not on Google's servers. That slowness is the point of the demo. |
| You pushed a change but the app looks the same | Wait a minute and refresh. If it still looks old: **Manage app → ⋮ → Reboot app**, then watch the build log. |
