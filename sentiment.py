import streamlit as st
from transformers import pipeline

# Load sentiment model
pipe = pipeline(
    "text-classification",
    model="cardiffnlp/twitter-roberta-base-sentiment-latest"
)

st.title("Sentiment Detector")

# Text box
text = st.text_area("Enter some text:")

# Button
if st.button("Detect Sentiment"):
    if text:
        result = pipe(text)[0]

        st.write("Sentiment:", result["label"])
        st.write("Confidence:", result["score"])
    else:
        st.warning("Please enter some text.")
