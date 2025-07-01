import streamlit as st

st.title("👫 Студенческий совет общежития СПбГЭУ №2")
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
        .highlight-blue-2 {
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
        <p><b>Студенческий совет общежития</b> является органом студенческого самоуправления в общежитии СПбГЭУ, 
        образованным по инициативе обучающихся в целях учета мнения обучающихся по вопросам реализации молодежной 
        политики и воспитательной деятельности в сфере социальной поддержки и социальной защиты обучающихся, 
        проживающих в общежитиях, и утвержденный решением администрации Университета.</p> 
        <p>Целями деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются формирование у 
        обучающихся активной гражданской позиции, сознательного и ответственного отношения к возможностям своей 
        социальной самоорганизации и культурно-нравственного саморазвития, развитие умений и навыков самоуправления 
        и подготовка обучающихся к компетентному и ответственному участию в жизни общества.</p> 
    </div>
            """, unsafe_allow_html=True)

st.markdown("""
    <div class="colored-container">
            <div class="highlight-blue">
                <div class="text-indent-content">
                    <p><b>Задачами деятельности органов студенческого самоуправления в общежитиях СПбГЭУ являются:</b></p>
                </div>
            </div>
        <p>—  учет мнения обучающихся, проживающих в общежитии;</p>
        <p>—  организация взаимодействия администрации СПбГЭУ и студенческих общежитий в части улучшения 
        жилищных условий проживания обучающихся совместно с ПО;</p>
        <p>—  содействие обучающимся в решении социальных вопросов, связанных с проживанием в общежитии 
        совместно с ПО;</p>
        <p>—  организация просветительских, культурно-досуговых, спортивно-оздоровительных и адаптационных 
        мероприятий для обучающихся, проживающих в общежитии;</p>
        <p>—  противодействие деструктивной идеологии в студенческой среде.</p>
    </div>
            """, unsafe_allow_html=True)
st.divider()

st.header("Председатель студенческого совета")
col1, col2 = st.columns([1, 3])
with col1:
    st.image("администрация_ч27/председатель_ч27.jpg", width=250)
with col2:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-green">
                <div class="text-indent-content">
                    <h3>Староста общежития</h3> 
                </div>
            </div>
            <p><b>Кейглер Илья Сергеевич</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://vk.com/keygler_27" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://t.me/keygler_27" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
            </div>
            <p>📞 <a href="tel:+79527017929">+79527017929</a></p>
        </div>
        """, unsafe_allow_html=True)
st.divider()

st.header("Старосты")

# 2 ЭТАЖ
col7, col8 = st.columns([1, 3])
with col7:
    st.image("администрация_ч27/староста_2_ч27.jpg", width=250)
with col8:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue-2">
                <div class="text-indent-content">
                    <h3>Староста 2 этажа</h3> 
                </div>
            </div>
            <p><b>Петришина Елизавета Олеговна</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://vk.com/eli.petrishina" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://t.me/ElizavetkaP" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
            </div>
            <p>📞 <a href="tel:+79833868796">+79833868796</a></p>
        </div>
        """, unsafe_allow_html=True)

# 3 ЭТАЖ
col9, col10 = st.columns([1, 3])
with col9:
    st.image("администрация_ч27/староста_3_ч27.jpg", width=250)
with col10:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue-2">
                <div class="text-indent-content">
                    <h3>Староста 3 этажа</h3> 
                </div>
            </div>
            <p><b>Обухов Марк Алексеевич</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://vk.com/luxxes.offc" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://t.me/makintosh777" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
            </div>
            <p>📞 <a href="tel:+79969187449">+79969187449</a>, <a href="tel:+79650502403">+79650502403</a></p>
        </div>
        """, unsafe_allow_html=True)

# 4 ЭТАЖ
col11, col12 = st.columns([1, 3])
with col11:
    st.image("администрация_ч27/староста_4_ч27.jpg", width=250)
with col12:
    st.markdown("""
        <div class="colored-container">
            <div class="highlight-blue-2">
                <div class="text-indent-content">
                    <h3>Староста 4 этажа</h3> 
                </div>
            </div>
            <p><b>Бойко Екатерина Александровна</b></p>
            <br>
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://vk.com/karrrrrrenn" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-vk"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в VK</p>
            </div>
            <div style="display: flex; align-items: center; gap: 10px; margin: 10px 0;">
                <a href="https://t.me/karrrrrrenn" target="_blank" style="margin-left: 5px; font-size: 25px;">
                    <i class="fab fa-telegram"></i>
                </a>
                <p style="margin: 0; font-size: 23px;">Связаться в TG</p>
            </div>
            <p>📞 <a href="tel:+79500714190">+79500714190</a></p>
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
