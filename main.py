import game

surah = game.pick_sura_j30_plus_fatiha()
max_aya = surah["nAyah"]
# print(surah)

score = 0
cur_aya_idx = 0
correct = True
while correct and cur_aya_idx < max_aya:
    correct = game.new_game(surah,cur_aya_idx)
    if correct:
        score += 1
        cur_aya_idx +=1

print(f"Permainan berakhir, skor anda: {score}")