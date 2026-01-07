import streamlit as st
from transformers import pipeline
from PIL import Image, ImageDraw, ImageFont
import torch
import time
from app_header import sidebar_menu

# 1. 페이지 설정
st.set_page_config(page_title="AI Vision Tool", layout="centered")

# 2. 사이드바 메뉴 (기존 기능 유지)
top_k_count = sidebar_menu()


# 3. 모델 로드 함수 (분류용 & 탐지용)
@st.cache_resource
def load_models(task_type):
    device_id = 0 if torch.cuda.is_available() else -1
    if task_type == "Classification":
        return pipeline("image-classification", model="google/vit-base-patch16-224", device=device_id)
    else:
        return pipeline("object-detection", model="facebook/detr-resnet-50", device=device_id)


# 4. 메인 UI
st.title("🤖 AI 비전 통합 분석기")
task = st.radio("수행할 작업을 선택하세요", ["Classification (분류)", "Object Detection (탐지)"], horizontal=True)

# 모델 로드
task_key = "Classification" if "Classification" in task else "Detection"
model_pipeline = load_models(task_key)

uploaded_file = st.file_uploader("이미지 업로드", type=['jpg', 'jpeg', 'png', 'jfif', 'webp'])

if uploaded_file is not None:
    # 이미지 준비
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="원본 이미지", use_container_width=True)

    alert_placeholder = st.empty()

    # --- 분석 실행 ---
    with st.spinner(f'{task_key} 분석 중...'):
        results = model_pipeline(image)

    alert_placeholder.success(f"🚀 {task_key} 완료!")

    # --- 결과 시각화 ---
    if task_key == "Classification":
        st.subheader("📊 분류 결과")
        for res in results[:top_k_count]:
            col1, col2 = st.columns([1, 4])
            with col1: st.write(f"**{res['label']}**")
            with col2:
                st.progress(res['score'])
                st.write(f"{round(res['score'] * 100, 2)}%")

    else:
        st.subheader("🎯 탐지된 객체 위치")
        # 이미지 위에 박스 그리기
        draw = ImageDraw.Draw(image)

        # 폰트 설정 (기본 폰트 사용, 리눅스/윈도우 호환)
        try:
            font = ImageFont.load_default()
        except:
            font = None

        for res in results:
            box = res['box']
            label = res['label']
            score = res['score']

            # 박스 그리기 [xmin, ymin, xmax, ymax]
            draw.rectangle(
                [(box['xmin'], box['ymin']), (box['xmax'], box['ymax'])],
                outline="red",
                width=4
            )
            # 라벨 표시
            draw.text((box['xmin'], box['ymin'] - 10), f"{label} {round(score * 100, 1)}%", fill="red")

        # 박스가 그려진 이미지 출력
        st.image(image, caption="탐지 결과 이미지", use_container_width=True)

        # 탐지 목록 표기
        for res in results:
            st.write(f"📍 발견: **{res['label']}** (신뢰도: {round(res['score'] * 100, 2)}%)")

    time.sleep(3)
    alert_placeholder.empty()