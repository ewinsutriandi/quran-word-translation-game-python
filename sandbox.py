import loader

ayah_all = loader.load_ayah_all()
word_all = loader.load_word_all()

ayah_word_map = {}

for k,v in word_all.items():
    ayah_idx = str(v["ayah"])
    ayah_word = {"start":int(k), "end":int(k)}
    if ayah_idx in ayah_word_map:
        ayah_word = ayah_word_map[str(ayah_idx)]
        st_idx = int(ayah_word["start"])
        ed_idx = int(ayah_word["end"])
        if int(k) < st_idx:
            ayah_word["start"] = int(k)
        if int(k) > ed_idx:
            ayah_word["end"] = int(k)    
    ayah_word_map[str(ayah_idx)] = ayah_word

for i in range(1,25):
    ayah_word = ayah_word_map[str(i)] 
    print(ayah_word)

import json

with open('qres/ayah-word-map.json', 'w') as fp:
    json.dump(ayah_word_map, fp, indent=4)