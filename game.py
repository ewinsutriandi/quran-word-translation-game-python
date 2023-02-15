import loader
import generators
import random

def pick_sura_j30_plus_fatiha():
    sura_j30 = loader.load_juz_amma_plus_fatiha()
    # prepare column
    # 114 / 4 => 29 rows
    row_cnt = 10
    keys = list(sura_j30.keys())
    # print("keys:",keys)    
    rows = []
    for i in  range(row_cnt):
        s_row = []
        for c in range(4):                        
            idx = i + (c * row_cnt)            
            if idx < 38:                
                key = keys[idx]
                # print("i c idx key:",i,c,idx,key,end=" ")
                sura = sura_j30[key]
                sura["key"] = key
                s_row.append(sura)
        rows.append(s_row)
    for row in rows:
        for s_row in row:
            print(f'{s_row["key"]:>3} {s_row["nama"]:<19}',end=" ")
        print()
    idx_select = input("Pilih surat: ")
    if idx_select in sura_j30:
        selected = sura_j30[idx_select]
        selected["idx"] = idx_select
        print(selected["nama"])
        return selected
    else:
        print("Nomor surat tidak ditemukan")
        return False

def new_simple_game(surah,difficulty="EASY"):    
    quiz_list = []
    generator = generators.GenerateEasyDiffQuizFromSingleSura
    if difficulty=="NORMAL":
        generator = generators.GenerateMidDiffQuizFromSingleSura
    quiz_list= generator(surah).generateQuizList()
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

