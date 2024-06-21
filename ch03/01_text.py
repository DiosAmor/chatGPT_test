import streamlit as st

st.title("This is Title")

st.header("This is Header")

st.subheader("This is Subheader")

st.caption("This is Caption")

sample_code = """
def function():
    print('Hello World')

"""
st.code(sample_code, language="python")

st.text("This is the general text")

st.markdown("streamlit support **markdown language**")
st.markdown("---")

# 컬러코드: blue, green, orange, red, violet
st.markdown(
    "텍스트의 색상을 :green[초록색]으로, 그리고 **:blue[파란색]** 볼트체로 설정할 수 있습니다."
)
st.markdown(
    ":green[$\sqrt{x^2+y^2}=1$] 와 같이 latex 문법의 수식 표현도 가능합니다 :pencil:"
)

# LaTex 수식 지원
st.latex(r"\sqrt{x^2+y^2}=1")
