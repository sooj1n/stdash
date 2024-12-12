import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('요청/ 처리 건수 (h)')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

#df

#TODO
#request_time, prediction_time 이용해 '%Y-%m-%d-%H' 형식
#즉 시간별 GROUPBY COUNT 하여 plt 차트 그려보기
df

df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d-%H')

df_time = df.groupby('request_time').size().reset_index(name='count')
df_time

# 데이터 로드 및 변환
df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d-%H')

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



# 요청자, 처리자 통계

df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['prediction_time'] = df['prediction_time'].dt.strftime('%Y-%m-%d-%H')

#def time_check():
df_diff = df[df['prediction_time'] != df['request_time']]
#df_diff.groupby('request_user').size().reset_index(name='user')
df_diff = df_diff.groupby('request_user').size().reset_index(name='count')
df_diff 

# 그래프 그리기1d
fig, ax = plt.subplots(figsize=(10,6))
#df_diff.plot(kind='bar', x='request_time', y='count', ax=ax)
#plt.plot(df_time.index, df_time['count'], 'ro-')
ax.pie(df_diff['count'], labels=df_diff['request_user'], autopct='%1.1f%%', startangle=90)
ax.set_title('Users experiencing processing problems')
#ax.set_xlabel('Users')
#ax.set_ylabel('count')
#plt.xticks(rotation=45)
#plt.tight_layout()

# Streamlit을 통해 차트 표시
st.pyplot(fig)
