import os
import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
from settingUp import yourKey
import time

def runDuckie(model,currentSessionHistory):
    def runDuckie(model, currentSessionHistory):
        convo = model
        st.title("Duckie 🦆")
        prompt = st.chat_input("Ask me something, or say 'History' to see our old chats!")

        if prompt:
            currentSessionHistory = currentSessionHistory

        if prompt == "History":
            st.markdown("Quack! Here is our convo so far!")
            st.markdown(currentSessionHistory)
        else:
            convo.send_message(prompt)
            with st.spinner('Thinking'):
                time.sleep(2)
            st.success("Success! Your input was: " + prompt)
            st.markdown(prompt)
            lastText = "" + convo.last.text
            currentSessionHistory.append("Prompt: " + prompt + " Response: " + lastText)
            st.markdown(convo.last.text)
            # Adds the history to the model
            convo.history.append(prompt)






