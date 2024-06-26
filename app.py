import streamlit as st
from langchain_community.llms import Ollama

# Initialize Ollama with the llama3 model
llm = Ollama(model="llama3")

# Set the title of your Streamlit app
st.title("Alzheimer's Caregiver Support Chatbot 🤖")

# Pre-defined questions
predefined_questions = [
    "How can I manage agitation and aggression in my loved one?",
    "What activities are beneficial for someone with Alzheimer's?",
    "How do I handle sundowning symptoms?",
    "What are the best ways to communicate with someone who has Alzheimer's?",
    "How can I take care of myself while caring for someone with Alzheimer's?",
]

# Dropdown menu for pre-defined questions
selected_question = st.selectbox("Select a common question or ask your own:", [""] + predefined_questions)

# Text area for user input
custom_prompt = st.text_area("Or ask a custom question or seek advice 🤝", height=100)

# Combine selected pre-defined question with custom input if provided
prompt = selected_question if not custom_prompt else custom_prompt

if st.button("Prompt"):
    if prompt:
        with st.spinner("Generating ... "):
            st.write(llm.invoke(prompt, stop=['<|eot_id|>']))
