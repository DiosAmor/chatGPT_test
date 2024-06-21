##### 기본 정보 입력 #####
# Streamlit 패키지 추가
import streamlit as st

# PDF reader
from PyPDF2 import PdfReader

# Langchain 패키지들
from langchain_openai import ChatOpenAI
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.chains.question_answering import load_qa_chain

import os
from dotenv import load_dotenv


##### 메인 함수 #####
def main():
    st.set_page_config(page_title="PDF analyzer", layout="wide")
    load_dotenv()
    st.session_state["OPENAI_API"] = os.getenv("OPENAI_API_KEY")
    if "flag" not in st.session_state:
        st.session_state["flag"] = True
    if "knowledge_base" not in st.session_state:
        st.session_state["knowledge_base"] = ""

    # PDF 파일 받기
    pdf = "Draft P802.11ah_D10.0.pdf"
    if st.session_state["flag"]:
        # PDF 파일 텍스트 추출하기
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        # 청크 단위로 분할하기
        text_splitter = CharacterTextSplitter(
            separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len
        )
        chunks = text_splitter.split_text(text)
        embeddings = OpenAIEmbeddings(openai_api_key=st.session_state["OPENAI_API"])
        st.session_state["knowledge_base"] = FAISS.from_texts(chunks, embeddings)
        st.session_state["flag"] = False

    st.markdown("---")
    st.subheader("802.11ah에 대해서 질문을 입력하세요")
    # 사용자 질문 받기
    user_question = st.text_input("802.11ah 표준 문서에 근거하여 답변해드립니다.")
    if user_question:
        # 임베딩/ 시멘틱 인덱스

        docs = st.session_state["knowledge_base"].similarity_search(user_question)

        # 질문하기
        llm = ChatOpenAI(
            temperature=0,
            openai_api_key=st.session_state["OPENAI_API"],
            max_tokens=2000,
            model_name="gpt-3.5-turbo",
            request_timeout=120,
        )
        chain = load_qa_chain(llm, chain_type="stuff")
        response = chain.run(input_documents=docs, question=user_question)
        # 답변결과
        st.info(response)


if __name__ == "__main__":
    main()
