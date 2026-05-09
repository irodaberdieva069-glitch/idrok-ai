import streamlit as st

# Sahifa sozlamalari
st.set_page_config(
    page_title="IDROK AI",
    page_icon="🧠",
    layout="wide"
)

# Zamonaviy dizayn uchun CSS
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button {
        width: 100%;
        border-radius: 8px;
        height: 3em;
        background-color: #2e7bcf;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #1e5ba0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .question-box {
        background-color: #161b22;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 10px;
        border-left: 5px solid #2e7bcf;
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    st.title("🧠 IDROK AI — Professional Test Platformasi")
    st.markdown("---")

    # Savollar bazasi (Har bir fanda 20 tadan, jami 80 ta)
    database = {
        "IT": [
            ["Python'da 'GIL' nima?", "Global Interpreter Lock"], ["O(n log n) murakkablikka ega saralash?", "Merge sort"],
            ["HTTP 403 xatosi?", "Forbidden"], ["NoSQL bazaga misol?", "MongoDB"], ["Dasturlashda 'DRY' nima?", "Don't Repeat Yourself"],
            ["Docker image-larni saqlash joyi?", "Docker Hub"], ["LIFO prinsipi qaysi strukturada?", "Stack"], ["DNS vazifasi?", "IPni nomga o'zgartirish"],
            ["API'da 'idempotentlik' nima?", "Natija o'zgarmasligi"], ["Python'da __init__ nima?", "Konstruktor"], ["O'zgarmas (immutable) tur?", "Tuple"],
            ["Linux'da huquq o'zgartirish?", "chmod"], ["Frontend asosi?", "HTML"], ["Git'da vaqtincha saqlash?", "stash"],
            ["TCP va UDP farqi?", "Ulanishni tekshirish"], ["RAM nima?", "Tezkor xotira"], ["CPU miyasi?", "Yadro"],
            ["K8s nima?", "Kubernetes"], ["Machine Learning'da 'Overfitting'?", "O'ta moslashish"], ["JS nima?", "Dasturlash tili"]
        ],
        "Matematika": [
            ["1 dan 100 gacha sonlar yig'indisi?", "5050"], ["Log 2 asosga ko'ra 1024?", "10"], ["Sinus 90 gradusda?", "1"],
            ["Pifagor teoremasi?", "a^2+b^2=c^2"], ["Faktorial 5?", "120"], ["EBOB(48, 72)?", "24"], ["EKUK(12, 15)?", "60"],
            ["Pi qiymati (2 ta raqam)?", "3.14"], ["Hosila nima?", "O'zgarish tezligi"], ["Integrallash nima?", "Yuza hisoblash"],
            ["Oltin kesim nisbati?", "1.618"], ["Tub son bormi: 17?", "Ha"], ["2 ning 10-darajasi?", "1024"], ["Viyet teoremasi nimaga tegishli?", "Kvadrat tenglama"],
            ["Kombinatsiya 3 dan 2?", "3"], ["Doira yuzi?", "pi*r^2"], ["1 t silsila ayirmasi?", "d"], ["Geometrik silsila maxraji?", "q"],
            ["0 ga bo'lish?", "Aniqlanmagan"], ["Kvadrat ildiz 144?", "12"]
        ],
        "English": [
            ["Past Participle of 'Speak'?", "Spoken"], ["Antonym of 'Success'?", "Failure"], ["Synonym of 'Abundant'?", "Plentiful"],
            ["'Go' 2-shakli?", "Went"], ["Plural of 'Criterion'?", "Criteria"], ["Meaning of 'Break a leg'?", "Good luck"],
            ["Passive of 'He writes'?", "It is written"], ["Meaning of 'Under the weather'?", "Sick"], ["Antonym of 'Fragile'?", "Robust"],
            ["Synonym of 'Precise'?", "Accurate"], ["Oxford Comma nima?", "Vergul"], ["Plural of 'Phenomenon'?", "Phenomena"],
            ["Suffix for 'Friend'?", "-ship"], ["'Apple' tarjimasi?", "Olma"], ["Future Perfect?", "Will have + V3"],
            ["Who wrote 'Hamlet'?", "Shakespeare"], ["Bilingual nima?", "Ikki tilli"], ["Opposite of 'Fast'?", "Slow"],
            ["Synonym of 'Resilient'?", "Strong"], ["Gerund nima?", "V+ing"]
        ],
        "Rus tili": [
            ["Что такое 'Подлежащее'?", "Ega"], ["Антоним 'Правда'?", "Ложь"], ["Сколько падежей?", "6"],
            ["Синоним 'Красивый'?", "Прекрасный"], ["Что изучает 'Фонетика'?", "Звуки"], ["Род слова 'Метро'?", "Средний"],
            ["Множественное 'Ребенок'?", "Дети"], ["Как пишется: 'Вкратце'?", "Вкратце"], ["Что такое 'Глагол'?", "Fe'l"],
            ["Антоним 'Щедрый'?", "Жадный"], ["Значение 'Бить баклуши'?", "Бездельничать"], ["Род слова 'Время'?", "Средний"],
            ["Вопрос Дательного падежа?", "Кому? Чему?"], ["Синоним 'Храбрый'?", "Смелый"], ["Часть речи 'Красиво'?", "Наречие"],
            ["Сколько букв в алфавите?", "33"], ["Антоним 'Трудолюбивый'?", "Ленивый"], ["Что такое 'Морфология'?", "So'z turkumlari"],
            ["Степени сравнения?", "2"], ["Вопрос Творительного падежа?", "Кем? Чем?"]
        ]
    }

    # Sidebar
    with st.sidebar:
        st.header("⚙️ Bo'limlar")
        subject = st.selectbox("Fanni tanlang:", list(database.keys()))
        st.write("---")
        st.info("Har bir fan 20 ta professional savoldan iborat.")

    # Main Layout
    col1, col2 = st.columns([3, 1])

    with col1:
        st.subheader(f"📍 {subject} Yo'nalishi")
        score = 0
        user_answers = []

        # Form orqali savollarni chiqarish
        with st.form(key='quiz_form'):
            for i, (q, a) in enumerate(database[subject], 1):
                st.markdown(f"<div class='question-box'><b>{i}. {q}</b></div>", unsafe_allow_html=True)
                ans = st.text_input("Javobingizni yozing", key=f"q_{subject}_{i}", label_visibility="collapsed")
                user_answers.append((ans, a))
                st.write("")

            submit = st.form_submit_button("Natijani ko'rish 🚀")

            if submit:
                for ua, ca in user_answers:
                    if ua.strip().lower() == ca.lower():
                        score += 1
                
                st.session_state.score = score
                st.session_state.submitted = True

    with col2:
        st.markdown("### 📊 Natijalar")
        if 'submitted' in st.session_state and st.session_state.submitted:
            st.metric("To'g'ri javoblar", f"{st.session_state.score}/20")
            percentage = (st.session_state.score / 20) * 100
            st.write(f"Samaradorlik: **{percentage}%**")
            
            if st.session_state.score >= 16:
                st.balloons()
                st.success("Siz dahosiz! 🥇")
            elif st.session_state.score >= 10:
                st.warning("Yaxshi, lekin yana o'qish kerak! 📚")
            else:
                st.error("Ko'proq tayyorlaning! ⚠️")
        else:
            st.info("Testni yakunlang va natijani ko'ring.")

if __name__ == "__main__":
    main()
