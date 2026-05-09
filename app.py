def idrok_ai_hard_mode():
    # Jami 80 ta qiyinlashtirilgan savol (Har bir yo'nalishda 20 tadan)
    data = {
        "IT": [
            ["O(n log n) murakkablikka ega saralash algoritmi?", "Merge sort"],
            ["Python'da 'GIL' nima?", "Global Interpreter Lock"],
            ["Docker konteyneri va VM o'rtasidagi asosiy farq?", "Yadro almashinuvi"],
            ["HTTP 403 xatosi nimani anglatadi?", "Forbidden"],
            ["Rekursiya nima?", "Funksiyaning o'ziga o'zi murojaati"],
            ["NoSQL bazaga misol keltiring?", "MongoDB"],
            ["Dasturlashda 'DRY' prinsipi nima?", "Don't Repeat Yourself"],
            ["Kubernetes nima vazifani bajaradi?", "Orkestratsiya"],
            ["Linux'da fayl huquqlarini o'zgartirish komandasi?", "chmod"],
            ["Git'da 'rebase' va 'merge' farqi nimada?", "Tarixni saqlash"],
            ["Zichlash algoritmi (lossless) nima?", "Ma'lumot yo'qotmasdan siqish"],
            ["TCP va UDP o'rtasidagi asosiy farq?", "Ulanishni tekshirish"],
            ["API'da 'idempotentlik' nima?", "Natija o'zgarmasligi"],
            ["Python'da __init__ nima?", "Konstruktor"],
            ["O'zgarmas (immutable) ma'lumot turi?", "Tuple"],
            ["Kriptografiyada 'Asimmetrik kalit' nima?", "Ochiq va yopiq kalit"],
            ["SQL'da 'JOIN' turlari nechta?", "4"],
            ["Dependency Injection nima?", "Bog'liqlikni kiritish"],
            ["Binary search qanday massivda ishlaydi?", "Saralangan"],
            ["Kompilyatsiya va interpretatsiya farqi?", "Tarjima qilish vaqti"]
        ],
        "Matematika": [
            ["1 dan 100 gacha sonlar yig'indisi?", "5050"],
            ["Logarifm 2 asosga ko'ra 1024?", "10"],
            ["Pifagor teoremasi formulasi?", "a^2 + b^2 = c^2"],
            ["Sinus 90 gradusda nechaga teng?", "1"],
            ["Tub sonlar cheksizligini kim isbotlagan?", "Evklid"],
            ["Faktorial 5 nechaga teng?", "120"],
            ["Hosila nima?", "O'zgarish tezligi"],
            ["Integrallash nima?", "Yuza hisoblash"],
            ["Oltin kesim nisbati taxminan?", "1.618"],
            ["Matritsaning determinanti 0 bo'lsa nima deyiladi?", "Maxsus"],
            ["Fibonachchi sonlari ketma-ketligi qanday boshlanadi?", "0, 1, 1, 2, 3, 5"],
            ["Kombinatorika: 3 ta elementdan 2 talik joylashtirish?", "6"],
            ["Doira uzunligi formulasi?", "2*pi*r"],
            ["Determinant nima?", "Matritsa sonli qiymati"],
            ["Viyet teoremasi nimaga tegishli?", "Kvadrat tenglama"],
            ["Arifmetik progressiya ayirmasi belgisi?", "d"],
            ["Geometrik progressiya maxraji belgisi?", "q"],
            ["Kompleks sonlar qanday qismdan iborat?", "Haqiqiy va mavhum"],
            ["Ehtimollar nazariyasida hodisa ehtimoli oralig'i?", "0 dan 1 gacha"],
            ["Nolga bo'lish natijasi?", "Aniqlanmagan"]
        ],
        "English": [
            ["Past Participle of 'Speak'?", "Spoken"],
            ["Antonym of 'Procrastinate'?", "Expedite"],
            ["Synonym of 'Abundant'?", "Plentiful"],
            ["Conditional Type 3 structure?", "If + had + V3, would have + V3"],
            ["Meaning of 'Break a leg'?", "Good luck"],
            ["What is an Oxford Comma?", "Comma before 'and'"],
            ["Passive voice of 'He writes a letter'?", "A letter is written"],
            ["Plural of 'Criterion'?", "Criteria"],
            ["Synonym of 'Resilient'?", "Strong"],
            ["Antonym of 'Fragile'?", "Robust"],
            ["Meaning of 'Under the weather'?", "Sick"],
            ["Correct spelling: 'Necessary' or 'Neccessary'?", "Necessary"],
            ["Which one is a conjunction: 'But' or 'Run'?", "But"],
            ["Definition of 'Metaphor'?", "Hidden comparison"],
            ["Past Continuous tense use?", "Ongoing past action"],
            ["Plural of 'Phenomenon'?", "Phenomena"],
            ["Prefix for 'Legal' to make it opposite?", "Il-"],
            ["Suffix for 'Act' to make it a person?", "-or"],
            ["Meaning of 'Once in a blue moon'?", "Rarely"],
            ["What is a Gerund?", "Verb + ing as a noun"]
        ],
        "Rus tili": [
            ["Что такое 'Подлежащее'?", "Ega"],
            ["Антоним слова 'Трудолюбивый'?", "Ленивый"],
            ["Сколько падежей в русском языке?", "6"],
            ["Синоним слова 'Красивый'?", "Прекрасный"],
            ["Что изучает 'Фонетика'?", "Звуки"],
            ["Существительное 'Кофе' какого рода?", "Мужской"],
            ["Множественное число слова 'Человек'?", "Люди"],
            ["Как пишется: 'Вкратце' или 'В кратце'?", "Вкратце"],
            ["Что такое 'Глагол'?", "Fe'l"],
            ["Антоним слова 'Щедрый'?", "Жадный"],
            ["К какому склонению относится слово 'Мама'?", "1-е"],
            ["Значение фразеологизма 'Бить баклуши'?", "Бездельничать"],
            ["Степени сравнения прилагательных?", "2"],
            ["Что такое 'Орфография'?", "Imlo"],
            ["Род слова 'Время'?", "Средний"],
            ["Вопрос Дательного падежа?", "Кому? Чему?"],
            ["Антоним 'Радость'?", "Грусть"],
            ["Синоним 'Храбрый'?", "Смелый"],
            ["Что такое 'Морфология'?", "So'z turkumlari"],
            ["Часть слова перед корнем?", "Приставка"]
        ]
    }

    print("--- IDROK AI HARD MODE ---")
    fan = input("Fanni tanlang (IT, Matematika, English, Rus tili): ").strip().title()

    if fan in data:
        score = 0
        questions = data[fan]
        print(f"\n{fan} fanidan qiyinlashtirilgan 20 talik test:\n")

        for i, (q, a) in enumerate(questions, 1):
            print(f"{i}. {q}")
            user_ans = input("Javobingiz: ").strip().lower()
            if user_ans == a.lower():
                print("To'g'ri! ✅")
                score += 1
            else:
                print(f"Xato! To'g'ri javob: {a} ❌")
            print("-" * 30)

        print(f"\nNATIJA: 20 tadan {score} ta to'g'ri.")
        if score > 15:
            print("Siz haqiqiy ekspertsiz! 🏆")
    else:
        print("Xato! Bunday fan mavjud emas.")

if __name__ == "__main__":
    idrok_ai_hard_mode()
