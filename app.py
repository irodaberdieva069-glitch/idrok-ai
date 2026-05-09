import streamlit as st

# Sahifa sozlamalari (iPad uchun moslangan)
st.set_page_config(page_title="IDROK AI", page_icon="🧠", layout="wide")

# Skrinshotdagi ABT.uz uslubidagi dizayn (CSS)
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .test-card {
        background: white; padding: 25px; border-radius: 15px;
        border-top: 10px solid #00B5AD; box-shadow: 0 4px 10px rgba(0,0,0,0.05);
        text-align: center; margin-bottom: 20px;
    }
    .stButton>button { width: 100%; border-radius: 8px; background-color: #00B5AD; color: white; }
    </style>
    """, unsafe_allow_html=True)

# Sarlavha
st.title("🧠 IDROK AI — Aqlli Ta'lim")

# Savollar bazasi
if 'score' not in st.session_state: st.session_state.score = 0

savollar = [
    {"s": "Neuralink loyihasi qaysi sohaga tegishli?", "v": ["Tibbiyot va IT", "Qurilish", "Transport"], "j": "Tibbiyot va IT", "t": "Bro, bu miyani kompyuterga ulash texnologiyasi!"},
    {"s": "Gepatit qaysi organni zararlaydi?", "v": ["Yurak", "Jigar", "O'pka"], "j": "Jigar", "t": "Gepatit asosan jigar to'qimalarini yallig'lantiradi."},
]

# Sidebar - Statistika
st.sidebar.header("📊 Natijalarim")
st.sidebar.metric("Yechilgan", len(savollar))
st.sidebar.metric("Ball", st.session_state.score)

# Asosiy interfeys (Skrinshotdagi kabi 3 ta blok)
tab1, tab2, tab3 = st.tabs(["🏠 Asosiy", "🏥 Tibbiyot & IT", "⚙️ Sozlamalar"])

with tab1:
    st.markdown('<div class="test-card"><h3>Xush kelibsiz!</h3><p>Yo\'nalishni tanlang va bilimingizni IDROK AI bilan oshiring.</p></div>', unsafe_allow_html=True)

with tab2:
    for i, item in enumerate(savollar):
        with st.expander(f"Savol #{i+1}"):
            st.write(item["s"])
            javob = st.radio("Javobni tanlang:", item["v"], key=f"q_{i}")
            if st.button("Tekshirish", key=f"btn_{i}"):
                if javob == item["j"]:
                    st.success("To'g'ri!")
                    st.session_state.score += 1
                else:
                    st.error(f"Xato! To'g'ri javob: {item['j']}")
                    st.info(f"💡 IDROK AI Tushuntirishi: {item['t']}")
