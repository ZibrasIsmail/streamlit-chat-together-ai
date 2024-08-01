import streamlit as st
from langchain_together import Together

st.title("🦜🔗 Quickstart App")
together_api_key = st.sidebar.text_input("Together API Key", type="password")

def generate_response(input_text):
    chat = Together(
        together_api_key=together_api_key,
        model="meta-llama/Llama-3-70b-chat-hf",
    )
    response = ""
    for chunk in chat.stream(input_text):
        response += chunk
        st.info(response)

with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What are the three key pieces of advice for learning how to code?",
    )
    submitted = st.form_submit_button("Submit")
    if not together_api_key:
        st.warning("Please enter your Together API key!", icon="⚠")
    if submitted and together_api_key:
        generate_response(text)