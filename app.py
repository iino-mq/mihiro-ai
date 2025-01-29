import openai
import streamlit as st

# StreamlitのSecretsからAPIキーを取得
openai.api_key = st.secrets[OPENAI_API_KEY]

st.title("カスタムAIチャットボット")

# ユーザー入力を取得
user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    # OpenAI APIへリクエスト（最新の書き方）
    response = openai.ChatCompletion.create(
        model="ft:gpt-4o-mini-2024-07-18:teammq::Av2dkXSy",
        messages=[{"role": "user", "content": user_input}]
    )

    # 回答を表示
    st.write(response["choices"][0]["message"]["content"])
