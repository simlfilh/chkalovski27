import streamlit as st
import streamlit.components.v1 as components

st.title("🏠 Видеообзор общежития СПбГЭУ №2 | пр-т Чкаловский, д. 27")
st.divider()

# https://vkvideo.ru/video-241063201_456239018

iframe_html = f"""
<iframe 
    src="https://vk.com/video_ext.php?oid=-241063201&id=456239018&hd=2" 
    width="640" 
    height="360" 
    frameborder="0" 
    allowfullscreen>
</iframe>
"""

components.html(iframe_html, height=380)
