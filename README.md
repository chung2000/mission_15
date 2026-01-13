# mission_17
mission_17

[Streamlit Cloud URL](https://mission15-lrpurpfnraysfwswf8aoia.streamlit.app/) : https://mission15-lrpurpfnraysfwswf8aoia.streamlit.app/

# 🖼️ AI 멀티 모델 광고 카피 생성기 (Streamlit App)

사용자가 입력한 제품명과 키워드를 바탕으로 **AWS Bedrock의 최신 LLM들**이 매력적인 광고 문구를 제안하는 **마케팅 자동화 웹 서비스**입니다.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://mission15-lrpurpfnraysfwswf8aoia.streamlit.app/)

> **👉 서비스 바로가기:** [https://mission15-lrpurpfnraysfwswf8aoia.streamlit.app/](https://mission15-lrpurpfnraysfwswf8aoia.streamlit.app/)

---

## 📅 프로젝트 개요

- **미션**: AWS Bedrock 환경에서 다양한 파운데이션 모델(Llama 3, EXAONE, Claude 등)을 연동하고, 비즈니스 목적에 맞는 광고 카피를 생성하는 AI 서비스를 구현합니다.
- **주요 기능**:
  - 🤖 **멀티 모델 스위칭**: Llama 3, EXAONE 등 원하는 AI 모델을 직접 선택하여 결과 비교
  - 🎭 **톤앤매너 맞춤 생성**: '감성적인', '긴박한', '유머러스한' 등 브랜드 이미지에 맞는 말투 설정
  - 🔑 **키워드 최적화**: 입력한 핵심 키워드를 문구 속에 자연스럽게 녹여내 마케팅 효과 극대화
  - ⚡ **실시간 생성**: 복잡한 설정 없이 단 몇 초 만에 3줄 이내의 SNS용 광고 카피 완성
  - 📱 **반응형 UI**: PC와 모바일 어디서든 간편하게 카피라이팅 업무 수행 가능

---

## 🖥️ 실행 화면

|          PC 메인 화면           |            결과 확인 화면            |
| :------------------------: | :-------------------------------: |
|  ![PC 메인](main_pc.png)   | ![결과 화면](result_view.png) |
| _제품 정보 및 모델 설정_ |      _생성된 광고 문구 확인_      |

---

## 🛠️ 기술 스택 및 사용 모델

이 서비스는 **Streamlit** 프레임워크를 기반으로 **AWS 클라우드 인프라**를 활용합니다.

### 1. 인프라 및 엔진
- **Cloud**: AWS Bedrock (Serverless LLM Service)
- **Framework**: Streamlit
- **SDK**: `boto3` (AWS SDK for Python)

### 2. 사용 가능한 AI 모델 (LLMs)
- **Meta Llama 3 70B**: 뛰어난 논리력과 창의적인 문장 구성 능력
- **LG EXAONE 3.0**: 한국어 문맥 이해도가 높고 자연스러운 비즈니스 작문 지원
- **Anthropic Claude 3 Haiku**: 빠른 속도와 효율적인 비용으로 가성비 높은 문구 생성



---

## 📝 개발 과정 및 트러블슈팅 (Troubleshooting)

프로젝트를 진행하며 겪었던 주요 이슈와 해결 과정을 기록합니다.

### Issue 1. 모델별 JSON 바디 규격 불일치
- **문제**: Bedrock의 `invoke_model` 사용 시, 모델 제작사마다 요구하는 입력 데이터(Key 이름)가 달라 `ValidationException`이 발생했습니다.
- **해결**: 모델별 전용 `Body` 생성 로직을 분기 처리했습니다. (Llama는 `prompt`, Claude는 `messages`, EXAONE은 특정 태그 구조 사용)

### Issue 2. 한국어 답변 품질 저하
- **문제**: 일부 글로벌 모델에서 광고 문구가 영어로 출력되거나 번역 투 문장이 생성되었습니다.
- **해결**: **시스템 프롬프트(System Instruction)**를 강화하여 "당신은 한국의 전문 마케터입니다"라는 역할을 부여하고, 출력 형식을 강제하여 품질을 높였습니다.

### Issue 3. AWS 인증 보안 문제
- **문제**: Streamlit Cloud 배포 시 AWS Access Key가 코드에 노출될 위험이 있었습니다.
- **해결**: Streamlit의 `Secrets` 관리 기능을 활용하여 환경 변수를 안전하게 주입하도록 구현했습니다.

---

## 📂 리포지토리 링크

소스 코드 및 상세 구현 내용은 아래 Github 저장소에서 확인하실 수 있습니다.
👉 **Github**: [https://github.com/chung2000/mission_17](https://github.com/chung2000/mission_17)

---

Copyright © 2026 Chung. All rights reserved.
