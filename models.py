from abc import ABC,abstractmethod

class QuizGenerator(ABC):
    '''
    Base class for quiz generator
    '''
    @abstractmethod
    def generateQuiz(self):
        pass

    @abstractmethod
    def generateQuizList(self):
        pass    

class Quiz():
    '''
    Base class for quiz
    '''
    def __init__(self,question: str,correct_answer: str):
        self.question = question
        self.correct_answer = correct_answer

class QuizMC(Quiz):
    '''(
    Multiple choice quiz
    ''' 
    def __init__(self,question: str,correct_answer: str,choices: list):
        super().__init__(question,correct_answer)
        self.choices = choices
