import streamlit as st
from streamlit_cropper import st_cropper
from PIL import Image

if "labels" not in st.session_state:
    st.session_state.labels = {}

st.title("PicAnnotator")

img = Image.open("datasets/道路.jpg")

# 画像を表示し、st_cropperで切り取り範囲を指定する
cropped_image = st_cropper(img, realtime_update=True, box_color="red")

col= st.columns([1, 3])
with col[0]:
    label_input = st.text_input(f"ラベル名を設定してね", "例）信号機")
    cropp_button = st.button("ラベル追加")
    if cropp_button:
        if label_input not in st.session_state.labels:
            st.session_state.labels[label_input] = []
        st.session_state.labels[label_input].append(cropped_image)
with col[1]:
    st.image(cropped_image)

st.markdown('<hr style="border-top: 3px solid #bbb;">', unsafe_allow_html=True)

for k, v in st.session_state.labels.items():
    st.header(k)
    col= st.columns(6)
    n = 0
    for imge in v:
        with col[n]:
            size = 100
            st.image(imge.resize((size, size)))
        n = (n + 1) % 6
    st.markdown('<hr style="border-top: 3px solid #bbb;">', unsafe_allow_html=True)
