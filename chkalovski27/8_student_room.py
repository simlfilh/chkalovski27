import streamlit as st

st.title("🚻 Студенческое пространство")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.image("рекреации_ч27/спортзал_ч27.jpg")
with col2:
    st.markdown("""
        <style>
            .colored-container {
               background-color: #FFFFFF; 
               border-radius: 10px;      
               padding: 20px;           
               margin-bottom: 20px;   
               color: black !important;
               line-height: 1.0;
               font-size: 21px;
            }
            .highlight-green {
                background-color: #C8E6C9;  
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-red {
                background-color: #FFCDD2;  
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding-left: 20px;
                margin-bottom: 20px;
                position: relative;
            }
            .text-indent-content {
                position: relative;
                color: black;
                line-height: 1.4;
            }
        </style>
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>1 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>💪 Спортзал</p> 
            <p>🕐 8:00 — 23:00</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)

col11, col12 = st.columns(2)
with col11:
    st.image("рекреации_ч27/коворкинг_ч27.jpg")
with col12:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-blue">
                    <div class="text-indent-content">
                        <h3>1 ЭТАЖ</h3> 
                    </div>
                </div> 
            <p>📚 Коворкинг</p>
            <p>🕐 24/7</p>
            <p>🔑 Ключ на охране</p> 
        </div>
                """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Беззубова Зоя Николаевна 👩🏼‍💼")
st.markdown("""
    <p>📞 <a href="tel:+78124589730">(812) 458-97-30</a></p>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("🆘 [Чат со студенческим советом](https://t.me/StudentCouncil_27_bot)")
