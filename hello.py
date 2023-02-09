import loader

all_sura = loader.load_surah_all()
surah = all_sura["1"]
print("Surah 1:",surah)
ayah_all = loader.load_ayah_all()
print("Ayah 1:",ayah_all["1"])

surah_ayahs = loader.load_surah_ayas(114)
for idx,item in surah_ayahs.items():
    print(idx,item)

ayahs = loader.load_surah_words(112)
for idx,v in ayahs.items():
    print(idx,v["text"])
    words = [(w["uthmani"],w["translation"]) for w in v["words"]]
    print(words)

j30 = loader.load_juz_amma()
for s in j30:
    print(s)
