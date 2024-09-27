import streamlit as st
import pandas as pd
import requests
from PIL import Image

st.markdown("# 🖼️ 이미지 처리 프로그램 결과 요약")
st.sidebar.markdown("# 🏠Home")

def load_data():
    url = 'http://43.202.66.118:8077/all'
    r = requests.get(url)
    d = r.json()
    df = pd.DataFrame(d)
    return df


# main()
img = Image.open('src/stdash/img/home.jpg')
st.image(img,width=1000)
