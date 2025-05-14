import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
# Set your API key here (or use an environment variable)
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

st.set_page_config(page_title="Lets ChatBot", page_icon="💬")
st.title("💬 Let's ChatBot")
st.caption("Powered by GPT-4o-mini")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful assistant."}
    ]

# Display previous messages
for msg in st.session_state.messages[1:]:
    st.chat_message(msg["role"]).markdown(msg["content"])

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Show user message
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get response from GPT-4o-mini
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",  # or gpt-3.5-turbo if needed
            messages=st.session_state.messages,
        )
        reply = response.choices[0].message.content

    except Exception as e:
        reply = f"❌ Error: {e}"

    # Show assistant message
    st.chat_message("assistant").markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})
