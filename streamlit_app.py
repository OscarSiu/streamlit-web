import streamlit as st
from st_functions import st_button, load_css
from PIL import Image

load_css()

st.write("[![Star](https://img.shields.io/github/stars/OscarSiu/NTRIP-Client?style=social)](https://github.com/OscarSiu/NTRIP-Client)")

#col1, col2, col3,col4,col5 = st.columns(5)
#col3.image(Image.open('profile.jpg'))
st.image('profile.JPG')
st.header('Siu Cheuk Yin Oscar')

st.info('Engineer | Robotics, Connected and Autonomous Vehicles, ROS, Computer Vision, CAD design')

icon_size = 20

st_button('linkedin', 'http://www.linkedin.com/in/siucheukyin', 'Follow me on LinkedIn', icon_size)
st_button('notion', 'https://www.notion.so/siucheukyin2022/World-Cup-2022-385584569dc948ed9b3943ac9d4f5e27', 'Follow me to Qatar World Cup 2022!', icon_size)
st_button('git', 'https://github.com/OscarSiu', 'Check out my works on Github', icon_size)
