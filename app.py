import streamlit as st
from app_header import sidebar_menu  # 파일명에서 함수를 가져옵니다.

import pandas as pd
import numpy as np
from PIL import Image
import torch

from transformers import pipeline

#페이지 기본설정
st.set_page_config(layout="wide", page_title="데이터분석 대시보드")

st.title("이미지 분류 웹 애플리케이션")
st.markdown("---")

# 1. 사이드바 호출 및 선택 값 받아오기
uploaded_file, chart_type = sidebar_menu()

@st.cache_resource
def load_model():
    # GPU 사용 가능 여부 확인 (0이면 GPU, -1이면 CPU)
    device_id = 0 if torch.cuda.is_available() else -1

    # task와 model을 각각 지정해줍니다.
    return pipeline(task="image-classification", model="google/vit-base-patch16-224", device=device_id)


#[메인] 데이터 처리 로직
if uploaded_file is not None:
    #df = pd.read_csv(uploaded_file)
    #st.success("파일 업로드 성공")
    st.toast('이미지 업로드가 완료되었습니다!', icon='✅')

    #st.image(uploaded_file)
    # width 파라미터에 픽셀 값을 숫자로 입력합니다.
    #st.image(uploaded_file, caption="600px 너비로 출력", width=600)
    # 2. 이미지 처리 및 출력
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드된 이미지", width=224)

    # 여기서 바로 모델 예측(Inference) 함수를 호출하면 됩니다.
    st.success("이제 분석을 시작할 수 있습니다.")

    st.button("분류하기")
    ##if st.button("분석하기"):
else:
    with st.spinner("AI 모델 로딩중..."):
        classifier = load_model()

    st.write("문장을 입력하면 긍정인지 부정인지 분석합니다.")

    user_input = st.text_area("분석할 텍스트 입력", "나는 AI 엔지니어링과정이 재미있습니다.")

    if st.button("분석하기"):
        if user_input:
            result = classifier(user_input)[0]
            label = result['label']
            score = result['score']

            col1, col2 = st.columns(2)
            with col1:
                st.metric("감성결과", label)
            with col2:
                st.metric("Socre", f"{score:.2%}")

            if label == "POSITIVE":
                st.success("긍정입니다")
            else:
                st.error("부정입니다")

