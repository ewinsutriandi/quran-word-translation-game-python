import loader
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

def new_game(surah, cur_aya_idx=0):
    ayahs = loader.load_surah_words_with_translation(surah["idx"])    
    aya_keys = list(ayahs.keys())
    
    score = 0
    lose = False    
      
    cur_ayah = ayahs[aya_keys[cur_aya_idx]]
    words = cur_ayah["words"]
    random.shuffle(words)
    words[0]["is_correct"] = True

    # cek jika ayat terdiri atas kurang dari 3 potongan kata
    add_aya_idx = cur_aya_idx
    additional_words = [] # menampung potongan kata tambahan
    while len(words) < 3:
        add_word_needed = 3 - len(words)
        print("word needed:",add_word_needed)                
        # jika masih ada ayat berikutnya
        word_candidates = []
        add_ayah = {}
        if add_aya_idx+1 < len(aya_keys):
            add_ayah = ayahs[aya_keys[add_aya_idx+1]]            
        else: # ambil ayat sebelumnya
            add_ayah = ayahs[aya_keys[add_aya_idx-1]]
        word_candidates = add_ayah["words"]
        cnt = 0
        random.shuffle(word_candidates)
        while cnt < add_word_needed and cnt < len(word_candidates):
            print(cnt,add_word_needed,len(word_candidates))
            word_exist = False
            for w in words:
                identical_text = w["uthmani"] == word_candidates[cnt]["uthmani"]
                identical_trans = w["translation"] == word_candidates[cnt]["translation"]
                if identical_text or identical_trans:
                    word_exist = True
                    break
            if not word_exist:
                additional_words.append(word_candidates[cnt])
            cnt += 1    
        words = words + additional_words
    selected_words = words[:3]
    for w in selected_words:
        print(w)
    print(cur_ayah["text"])    
    uth = "uthmani"
    trns = "translation"
    print(f"Pada ayat tersebut:{selected_words[0][uth]} memiliki arti?")

    choices = selected_words.copy()
    random.shuffle(choices)
    
    print(f"a. {choices[0][trns]} b. {choices[1][trns]} c. {choices[2][trns]}")    
    answer = input("Jawaban a/b/c: ")

    selected_choice = None
    if answer.lower() == "a":
        selected_choice = choices[0]
    elif  answer.lower() == "b":
        selected_choice = choices[1]
    elif  answer.lower() == "c":
        selected_choice = choices[2]
    
    # print(selected_choice)
    if "is_correct" in selected_choice:
        return True    
    return False

# surah = pick_sura_j30_plus_fatiha()
# new_game(surah)

