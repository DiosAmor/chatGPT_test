import streamlit as st
import openai
import os
from dotenv import load_dotenv

load_dotenv()


def askGpt(prompt):
    messages_prompt = [{"role": "system", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages_prompt
    )
    gptResponse = response["choices"][0]["message"]["content"]
    return gptResponse


def main():
    st.set_page_config(page_title="요약 프로그램")
    openai.api_key = os.getenv("OPENAI_API_KEY")

    st.header("📃요약 프로그램")
    st.markdown("---")

    text = st.text_area("요약 할 글을 입력하세요")
    if st.button("요약"):
        prompt = f"""
        **Instructions** :
    - You are an expert assistant that summarizes text into **Korean language**.
    - Your task is to summarize the **text** sentences in **Korean language**.
    - Your summaries should include the following :
        - Omit duplicate content, but increase the summary weight of duplicate content.
        - Summarize by emphasizing concepts and arguments rather than case evidence.
        - Summarize in 3 lines.
        - Use the format of a bullet point.
    -text : {text}
    """
        st.info(askGpt(prompt))


if __name__ == "__main__":
    main()
