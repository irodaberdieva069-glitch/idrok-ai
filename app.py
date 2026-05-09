import streamlit as st

# 1. Sahifa sozlamalari
st.set_page_config(page_title="IDROK AI", page_icon="🧠", layout="wide")

# 2. Dizayn (CSS) - iPad ekraniga moslangan
st.markdown("""
    <style>
    .main { background-color: #f0f2f6; }
    .stButton>button { width: 100%; border-radius: 10px; height: 3em; background-color: #00B5AD; color: white; font-weight: bold; }
    .test-container { background: white; padding: 20px; border-radius: 15px; border-left: 10px solid #00B5AD; margin-bottom: 20px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); }
    .sidebar-text { font-size: 18px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

# 3. Savollar Bazasi
data = {
    "Matematika": [
        {"s": "48 va 72 sonlarining EBOBini toping.", "v": ["12", "24", "36", "48"], "j": "24", "t": "Bro, 48=24*2 va 72=24*3. Eng katta umumiy bo'luvchi 24!"},
        {"s": "12 va 18 sonlarining EKUKini toping.", "v": ["36", "54", "72", "108"], "j": "36", "t": "12 va 18-ga bo'linadigan eng kichik son bu 36."},
        {"s": "24 sonining nechta natural bo'luvchisi bor?", "v": ["6", "8", "10", "12"], "j": "8", "t": "24 = 2^3 * 3^1. Bo'luvchilar soni: (3+1)*(1+1) = 8 ta."},
        {"s": "Tub sonni toping.", "v": ["1", "9", "15", "17"], "j": "17", "t": "17 faqat o'ziga va 1 ga bo'linadi."},
        {"s": "Eng kichik juft tub son qaysi?", "v": ["0", "2", "4", "6"], "j": "2", "t": "2 - dunyodagi yagona juft tub son, bro!"}
    ],
    "Tibbiyot": [
        {"s": "Inson tanasidagi eng kichik suyak qayerda?", "v": ["Burun", "Quloq", "Barmoq", "Tish"], "j": "Quloq", "t": "O'rta quloqdagi 'uzangi' suyagi eng kichigi hisoblanadi."},
        {"s": "Qonning qaysi hujayralari kislorod tashiydi?", "v": ["Leykotsitlar", "Eritrotsitlar", "Trombotsitlar"], "j": "Eritrotsitlar", "t": "Bro, qizil qon tanachalari (eritrotsitlar) kislorod tashiydi."},
        {"s": "Insulun gormoni qaysi organda ishlab chiqariladi?", "v": ["Jigar", "Oshqozon osti bezi", "Buyrak"], "j": "Oshqozon osti bezi", "t": "Qondagi shakarni aynan shu bez nazorat qiladi."}
    ],
    "Ingliz tili": [
        {"s": "She ___ to school every day.", "v": ["go", "goes", "going", "gone"], "j": "goes", "t": "Present Simple'da uchinchi shaxs (she) uchun -es qo'shiladi."},
        {"s": "I am interested ___ IT.", "v": ["in", "on", "at", "for"], "j": "in", "t": "Interested fe'li har doim 'in' predlogi bilan keladi."}
    ],
    "Rus tili": [
        {"s": "Какого рода слово 'Книга'?", "v": ["Мужской", "Женский", "Средний"], "j": "Женский", "t": "-а bilan tugagan so'zlar asosan ayol jinsida bo'ladi."},
        {"s": "Множественное число слова 'Друг'?", "v": ["Други", "Друзья", "Друзей"], "j": "Друзья", "t": "Bu so'zni yodlab olish kerak, do'stlar — друзья!"}
    ]
}

# 4. Sidebar va Statistika
st.sidebar.title("🧠 IDROK AI")
st.sidebar.markdown(f"**Foydalanuvchi:** {st.sidebar.text_input('Ismingiz:', 'Abdulaziz')}")
if 'score' not in st.session_state: st.session_state.score = 0
st.sidebar.metric("To'g'ri javoblar", st.session_state.score)

# 5. Asosiy Bo'lim
st.title("Bilimni shunchaki tekshirmang, uni anglang!")
fan_tanlovi = st.selectbox("Fanni tanlang:", list(data.keys()))

st.write(f"### {fan_tanlovi} yo'nalishi bo'yicha testlar")

for i, item in enumerate(data[fan_tanlovi]):
    with st.container():
        st.markdown(f'<div class="test-container">', unsafe_allow_html=True)
        st.write(f"**Savol {i+1}:** {item['s']}")
        javob = st.radio("Variantlar:", item['v'], key=f"radio_{fan_tanlovi}_{i}")
        
        if st.button(f"Tekshirish {i+1}", key=f"btn_{fan_tanlovi}_{i}"):
            if javob == item['j']:
                st.success("To'g'ri! Barakalla.")
                st.session_state.score += 1
            else:
                st.error(f"Xato! To'g'ri javob: {item['j']}")
                st.info(f"💡 **IDROK AI Tushuntirishi:** {item['t']}")
        st.markdown('</div>', unsafe_allow_html=True)
