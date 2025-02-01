# stdash
### 목적
- 이미지 처리 시스템의 요청/처리 결과를 알고 싶다.
- 클러스터 안에서 문제가 되는 요청/처리자를 알고 싶다. - 요청만 하고 처리 되지 않는 ...

### 공통
- API 가 동작 하지 않는 상황 ( BE Down ) 에서도 심각한 오류가 보이지 않아야 함
- 다시 말해 기본적인 기능은 동작 하도록 구성

### STEP 1
- https://github.com/dMario24/stdash/pull/1
- 파이썬과 판다스 우리가 익숙한 차트로 부터 시작하자
![image](https://github.com/user-attachments/assets/97df917e-bf5d-43f5-bc6b-86beb6e7e7d1)

# 참조
- https://streamlit.io/


# 시작코드
```python
import pandas as pd
import matplotlib.pyplot as plt
import requests

st.title('CNN JOB MON')

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    return d

data = load_data()
df = pd.DataFrame(data)

# TODO
# request_time, prediction_time 이용해 '%Y-%m-%d %H' 형식
# 즉 시간별 GROUPBY COUNT 하여 plt 차트 그려보기

#df['request_time'] = pd.to_datetime()
#df['request_time'].dt.strftime('%Y-%m-%d %H')
#df.groupby('ABC').size()

#plt.bar(
#plt.plot(
#plt.xlabel(

# 화면에 그리기
#st.pyplot(plt)
```

### RUN
- streamlit run src/stdash/app.py


### STEP 2
- [x] 요청자, 처리자간의 통계 / 불균형(누가 처리에 문제가 있는지 확인) VIEW 추가
- [x] [deploy](https://docs.streamlit.io/deploy/streamlit-community-cloud/get-started/quickstart)
- [x] [docker](https://docs.streamlit.io/deploy/tutorials/docker)
- [x] [muti pages](https://docs.streamlit.io/get-started/fundamentals/additional-features)
- [ ] streamlit chart

### STEP 3
- [x] file upload
- [ ] hotdog 적용
- https://stackoverflow.com/questions/76448350/post-request-with-parameter-as-a-streamlit-file-uploader-object-for-a-pdf-throws

### 참고 링크
- https://soojin1.tistory.com/24
  
