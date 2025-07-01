import streamlit as st

st.title("📲 Наши социальные сети")
st.divider()

st.markdown("""
    <style>
        .colored-container {
           background-color: #FFFFFF; 
           border-radius: 10px;     
           padding: 10px;          
           margin-bottom: 20px;     
           color: black !important;
           line-height: 1.0;
           font-size: 21px;
        }
        .highlight-green {
            background-color: #C8E6C9; 
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-red {
            background-color: #FFCDD2; 
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .highlight-blue {
            background-color: #B3E5FC;
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            position: relative;
        }
        .text-indent-content {
            position: relative;
            left: 20px;
            color: black;
            line-height: 1.4;
        }
    </style>
    <div class="colored-container">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div style="display: flex; align-items: center; gap: 20px;">
                <a href="https://t.me/Chkalovsky_27_bot" target="_blank">
                <i class="fab fa-telegram fa-2x"></i></a>
                <h3>БОТ Общежития №2.</h3>
            </div>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div style="display: flex; align-items: center; gap: 20px;">
                <a href="https://t.me/StudentCouncil_27_bot" target="_blank">
                <i class="fab fa-telegram fa-2x"></i></a>
                <h3>БОТ обращений к студенческому совету общежития №2.</h3>
            </div>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Беззубова Зоя Николаевна 👩🏼‍💼")
st.markdown("""
    <p>📞 <a href="tel:+78124589730">(812) 458-97-30</a></p>
            """, unsafe_allow_html=True)

st.markdown("🆘 [Чат со студенческим советом](https://t.me/StudentCouncil_27_bot)")
