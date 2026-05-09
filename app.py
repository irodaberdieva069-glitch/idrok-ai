import streamlit as st

# Sahifa sozlamalari
st.set_page_config(page_title="IDROK AI", page_icon="🧠")

def main():
    st.title("🧠 IDROK AI - Bilimlar platformasi")
    
    # Savollar bazasi
    data = {
        "IT": [
            ["Dasturlashda 'Clean Code' kitobi muallifi?", "Robert Martin"],
            ["Bitta CPU yadrosida bir vaqtda bir nechta oqim ishlashi?", "Multithreading"],
            ["LIFO prinsipi asosida ishlaydigan ma'lumotlar strukturasi?", "Stack"],
            ["IP manzillarni nomga o'zgartiruvchi xizmat?", "DNS"],
            ["Python'da dekoratorlar qaysi belgi bilan boshlanadi?", "@"],
            ["Git'da o'zgarishlarni vaqtincha saqlab turish?", "git stash"],
            ["SaaS qisqartmasining ma'nosi?", "Software as a Service"],
            ["'Big O' nima uchun ishlatiladi?", "Algoritm murakkabligini o'lchash"],
            ["Relatsion bo'lmagan MB?", "MongoDB"],
            ["VPN protokollaridan birini ayting?", "OpenVPN"],
            ["Shifrlashning eng keng tarqalgan standarti?", "AES"],
            ["Kubernetes qisqacha qanday yoziladi?", "K8s"],
            ["Xing (Cross-site scripting) qisqartmasi?", "XSS"],
            ["RAM va ROM orasidagi farq nima?", "RAM o'chuvchi xotira"],
            ["Python'da 'list comprehension' nima beradi?", "Sintaktik qulaylik"],
            ["Docker image-larni saqlash joyi?", "Docker Hub"],
            ["Machine Learning'da 'Overfitting' nima?", "Modelning o'ta moslashishi"],
            ["API test qilish uchun eng mashhur dastur?", "Postman"],
            ["Linux yadro (kernel) muallifi?", "Linus Torvalds"],
            ["Blockchain texnologiyasining asosi?", "Markazlashmagan reyestr"]
        ],
        "Matematika": [
            ["EBOB(48, 72) nechaga teng?", "24"],
            ["EKUK(12, 15, 20) nechaga teng?", "60"],
            ["Logarifm 3 asosga ko'ra 81?", "4"],
            ["Kvadrat tenglamaning diskriminant formulasi?", "D=b^2-4ac"],
            ["Sonning 0-darajasi har doim nechaga teng?", "1"],
            ["Uchburchakning yuzi (asos va balandlik orqali)?", "S=1/2*a*h"],
            ["Birinchi 10 ta toq sonlar yig'indisi?", "100"],
            ["Sinusoida funksiyasining davri?", "2pi"],
            ["Sfera hajmi formulasi?", "4/3*pi*r^3"],
            ["Vektorlarning skalyar ko'paytmasi natijasi?", "Son"],
            ["Oltin kesim soni (F)?", "1.618"],
            ["Arifmetik progressiya n-hadi?", "a1+(n-1)d"],
            ["Matritsani teskari matritsaga ko'paytirsa nima chiqadi?", "Birlik matritsa"],
            ["Integralda aniqmas integral belgisi ostidagi funksiya?", "Boshlang'ich funksiya"],
            ["Ehtimollik: bitta tanga tashlanganda gerb tushishi?", "0.5"],
            ["Natural sonlar to'plami qaysi harf bilan belgilanadi?", "N"],
            ["Tangensning hosilasi?", "1/cos^2(x)"],
            ["Pifagor sonlaridan biri (3, 4, ...)?", "5"],
            ["Kombinatsiya formulasi (C n dan k)?", "n!/(k!(n-k)!)"],
            ["Yevklid algoritmi nima uchun kerak?", "EBOBni topish"]
        ],
        "English": [
            ["Opposite of 'Success'?", "Failure"],
            ["Synonym of 'Precise'?", "Accurate"],
            ["Past simple of 'Buy'?", "Bought"],
            ["What is the plural of 'Sheep'?", "Sheep"],
            ["Someone who speaks two languages?", "Bilingual"],
            ["Meaning of the idiom 'Under the weather'?", "Feeling sick"],
            ["Which modal verb expresses strong obligation?", "Must"],
            ["The longest word in English dictionary (starts with P)?", "Pneumonoultramicroscopicsilicovolcanoconiosis"],
            ["Suffix for 'Friend' to make an abstract noun?", "-ship"],
            ["What part of speech is 'Quickly'?", "Adverb"],
            ["Passive voice of 'She cleans the room'?", "The room is cleaned"],
            ["What is a 'Synonym'?", "Same meaning word"],
            ["Comparative form of 'Bad'?", "Worse"],
            ["Superlative form of 'Far'?", "Farthest"],
            ["Which country is 'Down Under'?", "Australia"],
            ["What does 'CEO' stand for?", "Chief Executive Officer"],
            ["Meaning of 'Break a leg'?", "Good luck"],
            ["A person who hates spending money?", "Miser"],
            ["Future perfect structure?", "Will have + V3"],
            ["Who wrote 'Hamlet'?", "Shakespeare"]
        ],
        "Rus tili": [
            ["Антоним слова 'Правда'?", "Ложь"],
            ["Синоним слова 'Трудный'?", "Сложный"],
            ["Род слова 'Метро'?", "Средний"],
            ["Вопрос Родительного падежа?", "Кого? Чего?"],
            ["Сколько букв в русском алфавите?", "33"],
            ["Как называется часть слова после корня?", "Суффикс"],
            ["Главный член предложения, отвечающий на вопрос 'Что делать'?", "Сказуемое"],
            ["К какому склонению относится слово 'Дерево'?", "2-е"],
            ["Множественное число слова 'Ребенок'?", "Дети"],
            ["Значение слова 'Уникальный'?", "Единственный"],
            ["Правописание: 'ЖИ-ШИ' пишется с какой буквой?", "И"],
            ["Как пишется: 'По-русски' или 'По русски'?", "По-русски"],
            ["Синоним слова 'Огромный'?", "Колоссальный"],
            ["Вопрос Творительного падежа?", "Кем? Чем?"],
            ["Что такое 'Омонимы'?", "Слова, пишущиеся одинаково, но с разным значением"],
            ["Антоним слова 'Смелый'?", "Трусливый"],
            ["Часть речи, обозначающая признак предмета?", "Прилагательное"],
            ["Как называется разговор двух лиц?", "Диалог"],
            ["Местоимение 1-го лица единственного числа?", "Я"],
            ["Что изучает Лексикология?", "Словарный состав языка"]
        ]
    }

    # Fan tanlash
    subject = st.sidebar.selectbox("Fanni tanlang:", list(data.keys()))
    
    st.subheader(f"Fan: {subject}")
    
    score = 0
    with st.form(key='quiz_form'):
        user_answers = []
        for i, (q, a) in enumerate(data[subject], 1):
            st.write(f"**{i}. {q}**")
            ans = st.text_input(f"Javobingiz ({i})", key=f"q_{subject}_{i}")
            user_answers.append((ans, a))
        
        submit = st.form_submit_button("Natijani ko'rish")
        
        if submit:
            for user_ans, correct_ans in user_answers:
                if user_ans.strip().lower() == correct_ans.lower():
                    score += 1
            
            st.success(f"Siz 20 tadan {score} ta to'g'ri topdingiz!")
            st.progress(score / 20)
            
            if score >= 16:
                st.balloons()
                st.write("Dahosiz! 🏆")

if __name__ == "__main__":
    main()
