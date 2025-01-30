import openai
import streamlit as st

# StreamlitのSecretsからAPIキーを取得
openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("Mihiro-4o-mini - The Slow")

# パラメータ調整用のスライダーを追加
temperature = st.slider("Temperature", min_value=0.0, max_value=2.0, value=0.0, step=0.1)
top_p = st.slider("Top P", min_value=0.0, max_value=1.0, value=0.0, step=0.1)
max_tokens = st.slider("Max Tokens", min_value=16, max_value=2048, value=1024, step=16)

# 会話履歴を保持するためのリスト
messages = [{"role": "system", "content": "あなたはミヒロさんです。"}]

# ユーザー入力を取得
user_input = st.text_input("質問を入力してください")

if st.button("送信"):
    # ユーザーの入力を会話履歴に追加
    messages.append({"role": "user", "content": user_input})

    # OpenAI APIへリクエスト（最新の書き方）
    response = openai.chat.completions.create(
        model="ft:gpt-4o-mini-2024-07-18:teammq::Av2dkXSy",
        messages=messages,
        temperature=temperature,  # Temperatureパラメータを追加
        top_p=top_p,  # Top Pパラメータを追加
        max_tokens=max_tokens  # Max Tokensパラメータを追加
    )

    # 回答を会話履歴に追加
    messages.append({"role": "assistant", "content": response.choices[0].message.content})

    # 回答を表示（最新のアクセス方法）
    st.write(response.choices[0].message.content)

# 会話履歴を表示
st.text_area("会話履歴", value="\n".join([f"{m['role']}: {m['content']}" for m in messages]), height=400)
