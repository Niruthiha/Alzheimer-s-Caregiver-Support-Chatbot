import streamlit as st
from langchain_community.llms import Ollama

# Initialize Ollama with the llama3 model
llm = Ollama(model="llama3")

# Set the title of your Streamlit app
st.title("Alzheimer's Caregiver Support Chatbot 🤖")

# Text area for user input
prompt = st.text_area("Ask a question or seek advice 🤝", height=100)

if st.button("Prompt"):
    if prompt:
        with st.spinner("Generating ... "):
            st.write(llm.invoke(prompt, stop=['<|eot_id|>']))