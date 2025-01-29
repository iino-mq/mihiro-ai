import openai
import streamlit as st

openai.api_key = st.secrets["OPENAI_API_KEY"]

client = openai.Client(api_key=openai.api_key)


st.title("カスタムAIチャットボット")

user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    response = client.chat.completions.create(
        model="ft:gpt-4o-mini:your-org:custom:id",
        messages=[{"role": "user", "content": user_input}]
    )
    st.write(response.choices[0].message["content"])
