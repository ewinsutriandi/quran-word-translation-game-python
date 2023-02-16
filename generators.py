import loader
import random
from models import QuizGenerator,QuizMC

class GenerateEasyDiffQuizFromSingleSura(QuizGenerator):
    '''
    Generate multiple choice quiz from single surah
    Easy difficulty
    Randomized words order within ayah, but sorted by ayah
    '''
    def __init__(self,surah) -> None:
        self.surah = surah

    def generateQuiz(self):
        quiz_list = self.generateQuizList()
        random.shuffle(quiz_list)
        return quiz_list[0]
    
    def generateQuizList(self):
        quiz_list = []
        aya_quiz_list = generateSurahQuizListGroupedByAyah(self.surah)
        #print(aya_quiz_list)
        for aya_quiz in aya_quiz_list:            
            random.shuffle(aya_quiz)            
            quiz_list += aya_quiz    
        return quiz_list

class GenerateMidDiffQuizFromSingleSura(QuizGenerator):
    '''
    Generate multiple choice quiz from single surah
    Middle difficulty
    Randomized words order within surah
    '''
    def __init__(self,surah) -> None:
        self.surah = surah

    def generateQuiz(self):
        quiz_list = self.generateQuizList()
        random.shuffle(quiz_list)
        return quiz_list[0]
    
    def generateQuizList(self):
        quiz_list = []
        aya_quiz_list = generateSurahQuizListGroupedByAyah(self.surah)
        #print(aya_quiz_list)
        for aya_quiz in aya_quiz_list:                                    
            quiz_list += aya_quiz
        random.shuffle(quiz_list)    
        return quiz_list

class GenerateMidDiffQuizFromMultipleSura(QuizGenerator):
    '''
    Generate multiple choice quiz from multiple surah
    Middle difficulty
    Randomized words order within surah
    '''
    def __init__(self,list_surah) -> None:
        self.list_surah = list_surah

    def generateQuiz(self):
        quiz_list = self.generateQuizList()
        random.shuffle(quiz_list)
        return quiz_list[0]
    
    def generateQuizList(self):
        quiz_list = []
        for surah_idx,surah in self.list_surah.items():
            print(f"Loading surat no-{surah_idx}: {surah['nama']}")
            aya_quiz_list = generateSurahQuizListGroupedByAyah(surah)
            #print(aya_quiz_list)
            for aya_quiz in aya_quiz_list:                                    
                quiz_list += aya_quiz
        random.shuffle(quiz_list)    
        return quiz_list

def construct_choices(aya_idx,ayahs,aya_keys,words):
    add_aya_idx = aya_idx
    additional_words = [] # menampung potongan kata tambahan
    while len(words) < 3:
        add_word_needed = 3 - len(words)
        # print("word needed:",add_word_needed)                                
        word_candidates = []
        add_ayah = {}
        # jika masih ada ayat berikutnya
        if add_aya_idx+1 < len(aya_keys):
            add_ayah = ayahs[aya_keys[add_aya_idx+1]]
        else: # ambil ayat sebelumnya
            add_ayah = ayahs[aya_keys[add_aya_idx-1]]
        word_candidates = add_ayah["words"]
        random.shuffle(word_candidates)
        cnt = 0
        while cnt < add_word_needed and cnt < len(word_candidates):
            # print(cnt,add_word_needed,len(word_candidates))
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
    return words

def generateSurahQuizListGroupedByAyah(surah):
    ayahs = loader.load_surah_words_with_translation(surah["idx"])    
    aya_keys = list(ayahs.keys())
    max_aya = surah["nAyah"]
    uth = "uthmani"
    trns = "translation"
    aya_quiz_list = []
    for cur_aya_idx in range(max_aya):
        quiz_list = []
        cur_ayah = ayahs[aya_keys[cur_aya_idx]]
        words = cur_ayah["words"]
        pos = 0
        for word in words:
            # prepare quiz
            words_copy = words[pos:] + words[:pos]                                
            question = cur_ayah["text"]+"\n"
            question += f"Pada ayat tersebut:{word[uth]} memiliki arti?"
            answer = word[trns]
            # construct choices
            words_copy = construct_choices(cur_aya_idx,ayahs,aya_keys,words_copy)
            choices_words = words_copy[:3]
            choices = [word[trns] for word in choices_words]            
            quiz = QuizMC(question,answer,choices)
            pos += 1            
            quiz_list.append(quiz)
        aya_quiz_list.append(quiz_list)
    return aya_quiz_list