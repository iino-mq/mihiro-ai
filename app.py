import streamlit as st
from openai import OpenAI

client = OpenAI()

st.title("カスタムAIチャットボット")

user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    response = client.chat.completions.create(
        model="ft:gpt-4o-mini:your-org:custom:id",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.choices[0].message["content"])
