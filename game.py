import loader
import generators
import random

def start():    
    mode = pick_mode()    
    print("mode:", mode)
    if mode == 1:
        surah = False        
        # print(surah)
        while not surah:
            surah = pick_surah_j30_plus_fatiha()        
        new_simple_game(generators.GenerateMidDiffQuizFromSingleSura(surah))        
    elif mode == 2:
        list_surah = loader.load_juz_amma_plus_fatiha()
        # print(list_surah)
        new_simple_game(generators.GenerateMidDiffQuizFromMultipleSura(list_surah))
    elif mode == 3:
        surah = False        
        # print(surah)
        while not surah:
            surah = pick_surah_all()        
        new_simple_game(generators.GenerateMidDiffQuizFromSingleSura(surah))        
    elif mode == 4:
        list_surah = loader.load_surah_all()        
        new_simple_game(generators.GenerateMidDiffQuizFromMultipleSura(list_surah))
    else:
        print("Mode tidak dikenali")

def pick_mode():    
    print("PERMAINAN BELAJAR KOSAKATA AL-QURAN")
    print("Anda akan diminta memilih arti kosakata tertentu dari Al-Qur'an")
    print("Pilih sumber kosakata:")
    print("1. Satu surat pendek (juz amma + al-fatihah)")
    print("2. Seluruh surat pendek (juz amma + al-fatihah)")
    print("3. Satu surat (dari seluruh surat)")
    # print("4. Seluruh surat)")
    mode = 0
    valid_input = False    
    while not valid_input:
        mode = input("Pilihan anda(angka): ")
        if mode.isdigit():
            mode = int(mode)
            valid_input = mode>=1 and mode <=3                                
        if not valid_input:
            print("Gunakan angka dari 1 s.d 3")
    return mode

def pick_surah_all():
    surahs = loader.load_surah_all()
    # prepare column
    # 114 / 4 => 29 rows
    row_cnt = 29
    keys = list(surahs.keys())
    # print("keys:",keys)    
    rows = []
    for i in  range(row_cnt):
        s_row = []
        for c in range(4):                        
            idx = i + (c * row_cnt)
            # print(idx)            
            if idx < 114:                
                key = keys[idx]
                # print("i c idx key:",i,c,idx,key,end=" ")
                surah = surahs[key]
                surah["key"] = key
                s_row.append(surah)
        rows.append(s_row)
    print("Daftar surat Al Qur'an:")
    for row in rows:
        for s_row in row:
            print(f'{s_row["key"]:>3} {s_row["nama"]:<13}',end=" ")
        print()
    idx_select = input("Pilih surat (nomor): ")
    if idx_select in surahs:
        selected = surahs[idx_select]
        selected["idx"] = idx_select
        print(selected["nama"])
        return selected
    else:
        print("Nomor surat tidak ditemukan")
        return False

def pick_surah_j30_plus_fatiha():
    surah_j30 = loader.load_juz_amma_plus_fatiha()
    # prepare column
    # 114 / 4 => 29 rows
    row_cnt = 10
    keys = list(surah_j30.keys())
    # print("keys:",keys)    
    rows = []
    for i in  range(row_cnt):
        s_row = []
        for c in range(4):                        
            idx = i + (c * row_cnt)            
            if idx < 38:                
                key = keys[idx]
                # print("i c idx key:",i,c,idx,key,end=" ")
                surah = surah_j30[key]
                surah["key"] = key
                s_row.append(surah)
        rows.append(s_row)
    print("Daftar surat pada juz 30 plus Al-Fatihah:")
    for row in rows:
        for s_row in row:
            print(f'{s_row["key"]:>3} {s_row["nama"]:<13}',end=" ")
        print()
    idx_select = input("Pilih surat (nomor): ")
    if idx_select in surah_j30:
        selected = surah_j30[idx_select]
        selected["idx"] = idx_select
        print("Anda memilih:",selected["nama"])
        return selected
    else:
        print("Nomor surat tidak ditemukan")
        return False

def new_simple_game(generator:generators.QuizGenerator):        
    quiz_list= generator.generateQuizList()
    score = 0
    cur_quiz_idx = 0    
    correct = True
    while correct and cur_quiz_idx < len(quiz_list):
        quiz = quiz_list[cur_quiz_idx]
        print(quiz.question)
        choices = quiz.choices
        random.shuffle(choices)
        choice_map = {
            "a" : choices[0], "b" : choices[1], "c" : choices[2]
        }
        print(f"Pilih a. {choices[0]} b. {choices[1]} c. {choices[2]}")
        answer = input("Jawab (a/b/c):")        
        if answer in choice_map:
            correct = choice_map[answer] == quiz.correct_answer
        else:
            print("\_0_/")
            correct = False
        if correct:
            score += 1
            cur_quiz_idx +=1
        else:
            print(f"Jawaban benar: {quiz.correct_answer}")
    print(f"Permainan berakhir, skor anda: {score}")

# surah = pick_sura_j30_plus_fatiha()
# new_game(surah)

