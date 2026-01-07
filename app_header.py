# app_header.py
import streamlit as st


def sidebar_menu():
    #st.sidebar.title("🛠️ 설정 메뉴")

    # 사이드바 로고 이미지
    logo_url = "https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png"
    st.sidebar.image(logo_url, use_container_width=True)

    with st.sidebar:
        st.header("설정")
        uploaded_file = st.file_uploader("이미지 파일 업로드(224x224 크기)", type=['jpg', 'png'])

        chart_type = st.selectbox("차트 종류 선택", ["Line Chart", "Bar Chart", "Area Chart"])

    return uploaded_file, chart_type