import streamlit as st

st.title("👩🏽‍💻 Руководство общежития СПбГЭУ №2")
st.divider()

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
        <p><b>Администрация общежития</b> — это группа сотрудников, отвечающих за организацию проживания студентов, 
            поддержание порядка, безопасность и решение бытовых вопросов.</p>
        <br>
        <p>В администрацию общежития входят:</p>
        <p>• заведующий студенческим общежитием;</p>
        <p>• заместитель заведующего студенческим общежитием;</p>
        <p>• комендант;</p>
        <p>• заведующий хозяйственной частью.</p>
        <br>
        <p>В общежитии также организовано студенческое самоуправление в виде Студенческого совета общежития.</p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>Студенты могут обращаться к администрации общежития по широкому кругу вопросов, связанных с проживанием, бытовыми условиями и соблюдением правил.</p>
        <br>
        <p class="highlight-blue"><b>1.</b> Организационные вопросы.</p>
        <p class="highlight-blue"><b>2.</b> Бытовые проблемы.</p>
        <p class="highlight-blue"><b>3.</b> Коммунальные услуги и оплата.</p>
        <p class="highlight-blue"><b>4.</b> Безопасность.</p>
        <p class="highlight-blue"><b>5.</b> Инфраструктура и благоустройство.</p>
    </div>
            """, unsafe_allow_html=True)

col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация_ч27/заведующий_ч27.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
                <div class="highlight-green">
                    <div class="text-indent-content">
                        <h3> Заведующий студенческим общежитием</h3> 
                    </div>
                </div>
            <p><b>Беззубова Зоя Николаевна<b></p>  
            <br>  
            <p>📞 <a href="tel:+78124589730">(812) 458-97-30</a></a></p>
            <p>📩 <a href="mailto:bezzubova.z@unecon.ru">bezzubova.z@unecon.ru</a></p>
        </div>
                """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <div class="highlight-green">
            <div class="text-indent-content">
                <h3>🕐 Часы приёма студентов</h3> 
            </div>
        </div>
    <br>
    <p>ПН: 9:00 — 16:30</p>  
    <p>ВТ: 9:00 — 16:30</p>  
    <p>СР: приема нет</p>
    <p>ЧТ: 9:00 — 16:30</p>
    <p>ПТ: 9:00 — 16:00</p>
    <br>
    <p>🍜 ОБЕД: 12:00 — 12:30</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.markdown("""
    <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Паспортист</h3> 
                </div>
            </div>
        <p><b>🙍‍♂️️ Беззубов Николай Иванович<b></p>
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
        <p>🚪 Вся администрация общежития расположена на первом этаже общежития.</p>
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
