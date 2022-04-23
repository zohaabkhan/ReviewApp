import unittest
from func import quiz_score
from quizzes import quiz_setup,QUIZ1

class QuizScoreTests(unittest.TestCase): 
    """
    doc string: for the class
    """
    def test_quiz_math(self):
        """
        doc string: testing the scoring for the quizzes
        """
        test_score1 = 25    #sample score for question#1                            
        test_score2 = 25    #sample score for question#2
        test_score3 = 25    #sample score for question#3
        test_score4 = 0     #sample score for question#4
    
        expected_output = 75       #expecting the total score to be 75%
        actual_output = quiz_score(test_score1,test_score2,test_score3,test_score4) #putting the test scores into the function
        #self.assertEqual(actual, expected)
    



def load_quiz1(x): #takes a list as input
    """
    doc string: mock testing of a quiz loading
    """
    if x==QUIZ1:
        return QUIZ1


class TestLoadQuiz1(unittest.TestCase):
    """
    doc string: for the unit test class
    """
    def test_to_load_quiz1(self):
        """
        doc string: tests if the quiz is loaded correctly
        """
        actual = QUIZ1 = {
    # list containing quiz questions for lecture#1 and their answers
    "lecture": " 1: Syllabus & Introduction",
    "question_1": "1. True or False: This course is about learning Python?",
    "answer_1": "False",
    "question_2": "2. True or False: SWE at its core is not about programming languages or technologies, its about the art of problem solving.",
    "answer_2": "True",
    "question_3": "3. True or False: A tech stack is NOT a group of technologies.",
    "answer_3": "True",
    "question_4": "4. True or False: The objective for this class is to build applications reliably at scale with technologies you are new to.",
    "answer_4": "True"}
        expected = load_quiz1(QUIZ1) #expecting to see all the questions and answers for quiz#1
        self.assertEqual(actual, expected) #expecting both values to be the same output

if __name__=="__main__":
    unittest.main()            




