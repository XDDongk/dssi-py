import streamlit as st

st.title("我的Streamlit机器学习应用")

user_input = st.text_input("输入你的名字：")

if st.button("点击打招呼"):
    if user_input:
        st.write(f"你好，{user_input}！")
    else:
        st.write("请先输入你的名字！")
