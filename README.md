# stdash
## 프로젝트 개요

이 프로젝트는 이미지 판별기 테스트를 통해 수집된 AWS 서버의 DB 데이터를 활용하여 요청자와 처리자 간의 통계 및 불균형을 시각화하는 스트림릿 애플리케이션입니다.
![image](https://github.com/user-attachments/assets/ef21a0ab-dd4e-4d4b-a672-6adf945e3dc4)


## 주요 기능

- **요청/처리 건수 시각화**: 시간별 요청 건수를 막대 그래프로 표시합니다.
- **요청자/처리자 통계**: 요청자별 처리 불균형을 파이 차트로 시각화합니다.
- **멀티 페이지 구성**: 스트림릿의 멀티 페이지 기능을 활용하여 각 기능을 별도의 페이지로 구성하였습니다.

## 설치 및 실행 방법

### 필수 조건
- Python 3.x
- pip

### 패키지 설치
```bash
pip install streamlit pandas matplotlib requests
```

### 프로젝트 구조
```
프로젝트/
├── src/
│   └── stdash/
│       ├── app.py
│       ├── home.py
│       └── pages/
│           ├── total.py
│           └── user_stats.py
└── README.md
```

### 애플리케이션 실행
```bash
streamlit run src/stdash/app.py
```

## 사용된 기술 스택

- **프로그래밍 언어**: Python
- **프레임워크 및 라이브러리**:
  - Streamlit
  - Pandas
  - Matplotlib
  - Requests

## 주요 코드 설명

### 데이터 로드 함수
```python
import requests
import pandas as pd

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    df = pd.DataFrame(d)
    return df
```

![image](https://github.com/user-attachments/assets/a843eb3b-7a24-48e3-9cc0-194e4d1cfe61)


### 요청/처리 건수 시각화
```python
import matplotlib.pyplot as plt
import streamlit as st

df['request_time'] = pd.to_datetime(df['request_time'])
df['request_time'] = df['request_time'].dt.strftime('%Y-%m-%d-%H')

df_time = df.groupby('request_time').size().reset_index(name='count')

fig, ax = plt.subplots(figsize=(10,6))
df_time.plot(kind='bar', x='request_time', y='count', ax=ax)
plt.plot(df_time.index, df_time['count'], 'ro-')
ax.set_title('Requests by Date and Time')
ax.set_xlabel('Date and Time')
ax.set_ylabel('Number of Requests')
plt.xticks(rotation=45)
plt.tight_layout()

st.pyplot(fig)
```
![image](https://github.com/user-attachments/assets/4406e11a-bc1c-42c7-a937-a3ba07076490)

### 요청자/처리자 통계 시각화
```python
df['prediction_time'] = pd.to_datetime(df['prediction_time'])
df['prediction_time'] = df['prediction_time'].dt.strftime('%Y-%m-%d-%H')

df_diff = df[df['prediction_time'] != df['request_time']]
df_diff = df_diff.groupby('request_user').size().reset_index(name='count')

fig, ax = plt.subplots(figsize=(10,6))
ax.pie(df_diff['count'], labels=df_diff['request_user'], autopct='%1.1f%%', startangle=90)
ax.set_title('Users experiencing processing problems')

st.pyplot(fig)
```
![image](https://github.com/user-attachments/assets/0b60e280-1523-4485-831b-88bd6daf64fe)


## 멀티 페이지 구성

스트림릿의 멀티 페이지 기능을 활용하여 애플리케이션을 구성하였습니다. `home.py`에서 데이터 로드 함수를 정의하고, 각 페이지(`total.py`, `user_stats.py`)에서 해당 함수를 호출하여 데이터를 처리합니다.
![image](https://github.com/user-attachments/assets/775d67e0-81b4-4a05-a8ec-29467d70594d)


## 참고 자료
- [Streamlit 공식 문서](https://docs.streamlit.io/get-started/fundamentals/additional-features)

### 블로그 링크
- https://soojin1.tistory.com/24
  
