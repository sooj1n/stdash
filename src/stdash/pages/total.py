import streamlit as st
import pandas as pd
import requests
from home import load_data
import matplotlib.pyplot as plt

st.header("요청 / 처리 건수(h)")
#st.sidebar.markdown("# Page 2 ❄️")



df = load_data()


df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d-%H')

df_time = df.groupby('request_time').size().reset_index(name='count')


# 그래프 그리기1d
fig, ax = plt.subplots(figsize=(10,6))
df_time.plot(kind='bar', x='request_time', y='count', ax=ax)
plt.plot(df_time.index, df_time['count'], 'ro-')
ax.set_title('Requests by Date and Time')
ax.set_xlabel('Date and Time')
ax.set_ylabel('Number of Requests')
plt.xticks(rotation=45)
plt.tight_layout()

# Streamlit을 통해 차트 표시
st.pyplot(fig)

#st.bar_chart(
#    df_time,
#    x='request_time',
#    y='count',
#    #color=["#FF0000", "#0000FF"],  # Optional
#)


st.header('')
st.header('')
st.header('참고 데이터',divider='rainbow')
st.subheader("데이터")
df
st.subheader("시간 별 데이터")
df_time