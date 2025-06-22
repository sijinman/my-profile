# app.py

# 1. 필요한 도구를 가져옵니다 (import)
import streamlit as st
from PIL import Image #

# 2. st. 을 이용해서 화면에 글자와 그림을 추가합니다.
st.title("쁘니 요미 감자, 감쁘요 패밀리!")

st.header("우리 가족을 소개드릴게요.")

st.write("우리 첫째 쁘니!.")
st.write("쁘니는 5살이에요~ 이뻐서 쁘니에요. 하지만 남자라는 사실은 비밀.")
st.image(image=Image.open('images/pretty.jpg'), width 300)

st.write(둘째 요미! 4살이에요.)
st.image(image=Image.open('images/cute.jpg'), width=300)

st.wirte(마지막 감자! 3살이에요. 덩치는 제일 커요.)
st.image(image=Image.open('images/potato.jpg'), width=300)

# 3. 축하 풍선을 날려줍니다!
st.balloons()