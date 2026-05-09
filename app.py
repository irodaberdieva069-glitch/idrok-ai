import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(
    page_title="IDROK AI",
    page_icon="🎓",
    layout="wide"
)

# 2. Maxsus Dizayn (CSS)
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #2e7bcf;
        color: white;
        font-weight: bold;
        border: none;
        transition: 0.3s;
        font-size: 18px;
    }
    .stButton>button:hover {
        background-color: #1e5ba0;
        transform: scale(1.02);
    }
    .question-card {
        background-color: #161b22;
        padding: 20px;
        border-radius: 15px;
        margin-bottom: 15px;
        border-left: 6px solid #2e7bcf;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    </style>
    """, unsafe_allow_html=True)

def main():
    # 3. Savollar Bazasi (80 ta savol)
    database = {
        "IT": [
            ["Python'da 'GIL' nima?", "Global Interpreter Lock"], ["O(n log n) murakkablikka ega saralash?", "Merge sort"],
            ["HTTP 403 xatosi?", "Forbidden"], ["NoSQL bazaga misol?", "MongoDB"], ["Dasturlashda 'DRY' nima?", "Don't Repeat Yourself"],
            ["Docker image-larni saqlash joyi?", "Docker Hub"], ["LIFO prinsipi qaysi strukturada?", "Stack"], ["DNS vazifasi?", "IPni nomga o'zgartirish"],
            ["API'da 'idempotentlik' nima?", "Natija o'zgarmasligi"], ["Python'da __init__ nima?", "Konstruktor"], ["O'zgarmas (immutable) tur?", "Tuple"],
            ["Linux'da huquq o'zgartirish?", "chmod"], ["Frontend asosi?", "HTML"], ["Git'da vaqtincha saqlash?", "stash"],
            ["TCP va UDP farqi?", "Ulanishni tekshirish"], ["RAM nima?", "Tezkor xotira"], ["CPU miyasi?", "Yadro"],
            ["K8s nima?", "Kubernetes"], ["Machine Learning'da 'Overfitting'?", "O'ta moslashishi"], ["JS nima?", "Dasturlash tili"]
        ],
        "Matematika": [
            ["1 dan 100 gacha sonlar yig'indisi?", "5050"], ["Log 2 asosga ko'ra 1024?", "10"], ["Sinus 90 gradusda?", "1"],
            ["Pifagor teoremasi?", "a^2+b^2=c^2"], ["Faktorial 5?", "120"], ["EBOB(48, 72)?", "24"], ["EKUK(12, 15)?", "60"],
            ["Pi qiymati (2 ta raqam)?", "3.14"], ["Hosila nima?", "O'zgarish tezligi"], ["Integrallash nima?", "Yuza hisoblash"],
            ["Oltin kesim nisbati?", "1.618"], ["Tub son bormi: 17?", "Ha"], ["2 ning 10-darajasi?", "1024"], ["Viyet teoremasi?", "Kvadrat tenglama"],
            ["Kombinatsiya 3 dan 2?", "3"], ["Doira yuzi?", "pi*r^2"], ["Arifmetik silsila ayirmasi?", "d"], ["Geometrik silsila maxraji?", "q"],
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

    # 4. Sidebar va Logotip
    with st.sidebar:
        # Logotip (IDROK AI ramzi)
        st.image("https://cdn-icons-png.flaticon.com/512/3449/3449692.png", width=120)
        st.markdown("<h2 style='text-align: center;'>IDROK AI</h2>", unsafe_allow_html=True)
        st.write("---")
        
        # Fan tanlash
        subject = st.sidebar.selectbox("🎯 Yo'nalishni tanlang:", list(database.keys()))
        st.info(f"Hozirgi bo'lim: {subject}")
        st.write("---")
        st.caption("Abdulaziz Nematov tomonidan ishlab chiqildi.")

    # 5. Asosiy Qism
    st.title("🧠 Bilimingizni Sinovdan O'tkazing")
    st.markdown(f"### Yo'nalish: **{subject}**")
    
    col1, col2 = st.columns([3, 1])

    with col1:
        user_answers = []
        with st.form(key='idrok_quiz'):
            for i, (q, a) in enumerate(database[subject], 1):
                st.markdown(f"<div class='question-card'><b>{i}. {q}</b></div>", unsafe_allow_html=True)
                ans = st.text_input("Javobingiz:", key=f"input_{subject}_{i}", label_visibility="collapsed")
                user_answers.append((ans, a))
                st.write("")

            submit = st.form_submit_button("Natijani Tekshirish 🚀")

            if submit:
                score = 0
                for ua, ca in user_answers:
                    if ua.strip().lower() == ca.lower():
                        score += 1
                st.session_state.current_score = score
                st.session_state.is_submitted = True

    # 6. Natijalar paneli (O'ng tomon)
    with col2:
        st.markdown("### 📊 Ko'rsatkich")
        if 'is_submitted' in st.session_state and st.session_state.is_submitted:
            score = st.session_state.current_score
            st.metric("To'g'ri javob", f"{score}/20")
            
            progress = score / 20
            st.progress(progress)
            
            if score >= 18:
                st.balloons()
                st.success("A'lo! Siz haqiqiy mutaxassissiz! 🏆")
            elif score >= 10:
                st.warning("Yaxshi natija, yana ozroq harakat qiling! ✨")
            else:
                st.error("Ko'proq mutolaa qilish tavsiya etiladi. 📚")
        else:
            st.info("Testni yakunlab, 'Natijani Tekshirish' tugmasini bosing.")

if __name__ == "__main__":
    main()
