import generators as g
import game

surah = game.pick_sura_j30_plus_fatiha()

gen = g.GenerateMidDiffQuizFromSingleSura(surah)

ql = gen.generateQuizList()

for q in ql:
    print(q.question)
    print("jawaban:",q.correct_answer)
    print()