import os
import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
from settingUp import yourKey
import time
currentSessionHistory = []
def runDuckie(model):
    st.title("Duckie!")
    prompt = st.chat_input("Quack Quack Quack!")

    if "messages" not in st.session_state.keys():  # Initialize the chat message history
        st.session_state.messages = [
            {"role": "assistant", "content": "Ask me a question about Streamlit's open-source Python library!"}
        ]
        model.start_chat(history=[])
        with st.sidebar:
            st.title('History')

        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.write(message["Content"])





