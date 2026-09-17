import streamlit as st
import pandas as pd
import plotly.express as px

# --- 페이지 기본 설정 ---
st.set_page_config(page_title="영화 데이터 그래프 도감 2", layout="wide")

# --- 앱 제목 ---
st.title("영화 데이터 그래프 도감 2 - 분포와 관계")
st.write("1년간 박스오피스 10위권에 든 216편의 영화 데이터를 탐색합니다.")

# --- 데이터 로드 및 전처리 ---
@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_movies.csv"
    df = pd.read_csv(url)
    
    # 결측치 처리 및 장르 전처리: '|'로 여러 개가 적힌 경우 첫 번째 장르만 추출
    df['genre'] = df['genre'].fillna("알 수 없음")
    df['genre'] = df['genre'].apply(lambda x: str(x).split('|')[0])
    
    return df

df = load_data()

st.divider() # 구역 나누기

# --- 첫 번째 그래프: 장르별 영화 편수 (도넛 그래프) ---
st.subheader("1. 장르별 영화 편수")

# 장르별 빈도수 계산
genre_counts = df['genre'].value_counts().reset_index()
genre_counts.columns = ['장르', '편수']

# 플롯리(Plotly) 도넛 그래프 생성
fig_donut = px.pie(
    genre_counts, 
    names='장르', 
    values='편수', 
    hole=0.4, # 도넛 모양을 만들기 위한 중앙 구멍 설정
)

# 마우스를 올렸을 때(Hover) 편수와 비율이 명확히 보이도록 텍스트 템플릿 수정
fig_donut.update_traces(
    hovertemplate="<b>장르: %{label}</b><br>편수: %{value}편<br>비율: %{percent}"
)

# 그래프 출력
st.plotly_chart(fig_donut, use_container_width=True)

# 그래프 해석/인사이트 영역
st.info("💡 **이 그래프로 알 수 있는 것:** (여기에 장르 분포에 대한 핵심 분석을 한 문장으로 적어주세요.)")

st.divider() # 구역 나누기

# (필요에 따라 여기에 다음 그래프 코드를 추가하세요)
