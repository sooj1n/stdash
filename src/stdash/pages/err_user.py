import streamlit as st
import pandas as pd
import requests
from home import load_data
import matplotlib.pyplot as plt

st.header("요청/처리 불균형 사용자 분석")

df = load_data()

# 요청자, 처리자 통계

df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d-%H')

df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['prediction_time'] = df['prediction_time'].dt.strftime('%Y-%m-%d-%H')


df_diff = df[df['prediction_time'] != df['request_time']]
df_diff = df_diff.groupby('request_user').size().reset_index(name='count')

st.header('')
# 그래프 그리기
fig, ax = plt.subplots(figsize=(10,6))
ax.pie(df_diff['count'], labels=df_diff['request_user'],
        autopct='%1.1f%%', startangle=90)
ax.set_title('Users experiencing processing problems')

# 원이 완벽한 원형이 되도록 설정
ax.axis('equal')  

# Streamlit을 통해 차트 표시
st.pyplot(fig)


st.header('')
st.header('')
st.header('참고 데이터',divider='rainbow')
st.subheader("사용자 목록")
df_diff 