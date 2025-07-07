import streamlit as st

st.title("🏠 Общежитие СПбГЭУ №2")
st.divider()

st.subheader("Приветствуем вас, дорогие студенты, в нашем общежитии!")
st.subheader("Мы рады, что вы стали частью нашей дружной студенческой семьи!")
st.divider()

col1, col2 = st.columns(2)
with col1:
    st.markdown("""
        <style>
            .colored-container {
               background-color: #FFFFFF;  
               border-radius: 10px;      
               padding: 20px;            
               margin-bottom: 10px;      
               color: black !important;  
               line-height: 1.0;
               font-size: 21px;
            }
            .image-container {
               background-color: #FFFFFF; 
               border-radius: 10px;      
               padding: 20px;            
               margin-bottom: 10px;      
               height: 100%;           
               display: flex;
               align-items: center;     
               justify-content: center; 
            }
            .image-container img {
               max-width: 100%;
               max-height: 100%;
               border-radius: 5px;     
               object-fit: contain;    
            }
            .highlight-green {
                background-color: #C8E6C9; 
                border-radius: 10px;
                padding: 10px;
                margin-bottom: 10px;
                position: relative;
            }
            .highlight-blue {
                background-color: #B3E5FC;
                border-radius: 10px;
                padding: 10px;
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
            <h3>Адрес: Санкт-Петербург, Чкаловский пр-т, д. 27</h3>
                <div class="text-indent-content">
                    <p class="highlight-blue">Наиболее удобные маршруты:</p>
                </div>
            <br>
            <p>→ от м. Петроградская 10 минут пешком</p>  
            <p>→ от м. Чкаловская 10 минут пешком</p>  
            <br>
        </div>
                """, unsafe_allow_html=True)
with col2:
    st.markdown("""
        <div class="colored-container">
            <h3>Мы в Google Maps ⬇️</h3>
        </div>
                """, unsafe_allow_html=True)
    st.components.v1.html("""
        <iframe src="https://www.google.com/maps/embed?pb=!1m28!1m12!1m3!1d7987.415451973477!2d30.294856982375293!3d59.967747548874065!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!4m13!3e6!4m5!1s0x4696315ae8aaae41%3A0x71c197f2c712c2a2!2z0JzQtdGC0YDQviDQn9C10YLRgNC-0LPRgNCw0LTRgdC60LDRjywg0KHQsNC90LrRgi3Qn9C10YLQtdGA0LHRg9GA0LM!3m2!1d59.966535!2d30.31101!4m5!1s0x4696314fcabaea25%3A0x4df5379af82456c8!2z0KfQutCw0LvQvtCy0YHQutC40Lkg0L_RgNC-0YHQv9C10LrRgiwgMjcsINCh0LDQvdC60YIt0J_QtdGC0LXRgNCx0YPRgNCz!3m2!1d59.965905!2d30.2992991!5e0!3m2!1sru!2sru!4v1751375950695!5m2!1sru!2sru" 
            width="600" 
            height="430" 
            style="border:0; border-radius: 10px;" 
            allowfullscreen="" 
            loading="lazy" 
            referrerpolicy="no-referrer-when-downgrade">
        </iframe>
                    """, height=440)
st.divider()

col3, col4 = st.columns([1, 2])
with col4:
    st.markdown("""
        <div class="colored-container">
            <h3>Об общежитии</h3>
            <p>• Коридорный тип проживания (размещение по 2-4 человека в комнате)</p>  
            <p>• 4 этажа | 190 мест</p>
            <p>• На каждом этаже кухня, оснащенная газовыми плитами и столами</p>
            <p>• Общая прачечная</p>
            <p>• Интернет</p>
            <p>• 10-15 минут пешком от метро</p>
        </div>
                """, unsafe_allow_html=True)
with col3:
    st.image("здание_общежития_ч27.jpg",
             use_container_width=True)
st.divider()

st.markdown("*❗️ Пожалуйста, прежде чем связываться с администрацией, ознакомьтесь со всей информацией на сайте.*")
st.divider()

st.markdown("**Контакты для связи:**")
st.write("Заведующий общежитием: Беззубова Зоя Николаевна 👩🏼‍💼")
st.markdown("""
    <p>📞 <a href="tel:+78124589730,4295">(812) 458-97-30, доб. 4295</a></p>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("🆘 [Чат со студенческим советом](https://t.me/StudentCouncil_27_bot)")
