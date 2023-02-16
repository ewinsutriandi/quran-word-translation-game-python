import json

PATH = "qres/"

def load_surah_all():
    file = open(PATH+"surah.json")
    surah_all = json.load(file)
    surah_all = __inject_sura_translit_id_into_sura_list(surah_all)
    return surah_all

def __inject_sura_translit_id_into_sura_list(surah_all):
    file = open(PATH+"surah-translit-id.json")
    surah_tr = json.load(file)
    # print(surah_tr)
    for k,v in surah_tr.items():
        surah_all[k]["nama"] = v["nama"]
        surah_all[k]["arti_nama"] = v["arti_nama"]
    return surah_all

def load_juz_amma():
    start = 78
    end = 114
    surah_j30 = {}
    surah_all = load_surah_all()
    # surah_j30["1"] = surah_all["1"]
    # print(surah_j30,type(surah_j30))    
    for i in range(start,end+1):
        surah = surah_all[str(i)]        
        surah_j30[str(i)] = surah               
    return surah_j30

def load_juz_amma_plus_fatiha():
    start = 78
    end = 114
    surah_j30 = {}
    surah_all = load_surah_all()
    surah_j30["1"] = surah_all["1"]
    # print(surah_j30,type(surah_j30))    
    for i in range(start,end+1):
        surah = surah_all[str(i)]        
        surah_j30[str(i)] = surah               
    return surah_j30

def load_ayah_all():
    file = open(PATH+"ayah-uthmani.json")
    ayah_all = json.load(file)
    return ayah_all

def load_word_all():
    file = open(PATH+"word.json")
    word_all = json.load(file)
    return word_all

def load_word_trans_id():
    file = open(PATH+"id-word-trans.json")
    word_trans_all = json.load(file)
    return word_trans_all

def load_surah_ayas(idx):
    surah = load_surah_all()[str(idx)]
    ayah_all = load_ayah_all()
    ayahs = {str(aya_idx): ayah_all[str(aya_idx)] for aya_idx in range(surah["start"],surah["end"]+1)}
    # ayahs = [{str(aya_idx): ayah_all[str(aya_idx)]} for aya_idx in range(surah["start"],surah["end"]+1)]
    return ayahs

def __inject_translation_to_word(idx,word,trans):
    word["translation"] = trans[idx]
    #print(word["translation"])
    return word

def load_surah_words(idx):
    surah = load_surah_all()[str(idx)]
    ayahs = load_surah_ayas(str(idx))
    words = load_word_all()
    w_list= []
    for key in ayahs.keys():         
        print(key,":",ayahs[key])
        w_ayah = [w for a_idx,w in words.items() if w["ayah"] == int(key)]
        #print(w_ayah)
        ayahs[key] = {
            "text" : ayahs[key],
            "words": w_ayah}    
    return ayahs 

def load_surah_words_with_translation(idx):
    surah = load_surah_all()[str(idx)]
    ayahs = load_surah_ayas(str(idx))
    words = load_word_all()
    words_trans = load_word_trans_id()
    w_list= []
    for key in ayahs.keys():         
        # print(key,":",ayahs[key])        
        w_ayah = [__inject_translation_to_word(a_idx,w,words_trans) for a_idx,w in words.items() if w["ayah"] == int(key)]
        # print(w_ayah)
        ayahs[key] = {
            "text" : ayahs[key],
            "words": w_ayah}
    
    return ayahs 