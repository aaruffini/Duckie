import pathlib
import textwrap
import google.generativeai as genai
import streamlit as st
from settingUp import yourKey
import time

genai.configure(api_key=yourKey)

st.title("Duckie!")
model = genai.GenerativeModel("gemini-1.5-flash")
st.sidebar.markdown("Conversations")
chat = model.start_chat(
    history=[
        {"role": "user", "parts": "Hello"},
        {"role": "model", "parts": "Great to meet you. What would you like to know?"},
    ]
)
st.sidebar.button("New Conversation")
userPrompt = st.chat_input("Talk with Duckie!")
if userPrompt:
    response = chat.send_message(userPrompt)
    st.markdown(response.text)
    st.markdown("![Alt Text](https://i.giphy.com/media/v1.Y2lkPTc5MGI3NjExN3I2ZncwajJlMzk5MzJ0bDRoYmYwYXl2b20xbGc2dmx6MnNiYWdrNCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13nXJ5b7jn23ba/giphy.gif)")
