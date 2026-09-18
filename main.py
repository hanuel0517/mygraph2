# ── 그래프 2. 최고 흥행작 5편의 흥행 곡선 비교 ─────────────────────
st.header("2. 최고 흥행작 5편의 흥행 곡선 비교")

# 1. 영화별로 일관객 수를 모두 더한 뒤, 가장 큰 5편의 영화 이름을 골라냅니다.
top5_movies = df.groupby("영화명")["일관객"].sum().nlargest(5).index

# 2. 전체 데이터에서 이 5편의 영화 데이터만 걸러냅니다.
top5_df = df[df["영화명"].isin(top5_movies)].sort_values("날짜")

# 3. 하나의 선 그래프에 색(color)으로 영화를 구분하여 그립니다.
fig2 = px.line(top5_df, x="날짜", y="일관객", color="영화명", markers=True)
fig2.update_traces(hovertemplate="영화 %{data.name}<br>날짜 %{x|%Y-%m-%d}<br>관객 %{y:,}명<extra></extra>")

# Plotly는 기본적으로 범례를 클릭하면 해당 항목을 켜고 끌 수 있습니다.
st.plotly_chart(fig2, use_container_width=True)

st.caption("이 그래프로 알 수 있는 것: (이 기간 가장 흥행한 5편의 영화들의 관객 수 추이와 정점, 그리고 우측 범례를 클릭해 원하는 영화의 선만 켜고 끄면서 비교할 수 있습니다.)")

# ── 앞으로 그래프 3, 4, 5가 이 아래에 추가됩니다 ──────────
