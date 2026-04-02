import streamlit as st
import pickle
import re

model = pickle.load(open("model.pkl", "rb"))
tfidf = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return text

st.title("📩 Spam Message Classifier")
st.write("Enter a message to check if it's Spam or Not")

msg = st.text_input("Enter message")

if st.button("Predict"):
    cleaned = clean_text(msg)
    vector = tfidf.transform([cleaned])
    result = model.predict(vector)[0]

    if result == "spam":
        st.error("🚫 Spam Message")
    else:
        st.success("✅ Not Spam")