import loader

surah_words = loader.load_surah_words_with_translation("114")
for k,aya in surah_words.items():
    for l,word in aya.items():
        pass
        #print(word) 