QUIZ1 = {
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


QUIZ2 = { 
    # list containing quiz questions for lecture#2 and their answers
    "lecture": " 2: Git, Software Engineering",
    "question_1": "1. True or False: Git is a tool for collaborating with other people on writing code.",
    "answer_1": "True",
    "question_2": "2. True or False: Version control is the organized tracking and managing of a piece of code.",
    "answer_2": "True",
    "question_3": "3. True or False: git init is a command that creates a local repository?",
    "answer_3": "True",
    "question_4": "4. True or False: A PUSH says take my code from my local repository and PUSH it to the remote repo.",
    "answer_4": "True"}    


QUIZ3 = { 
    # list containing quiz questions and their answers
    "lecture": " 3: Python, Debugging",
    "question_1": "1. True or False: When you search for a video on Youtube, you are sending a request from the client to the server. The client is asking the Youtube server to get all the videos about a search topic. The server, then runs some processes on the search topic and returns all the data it found to the client.",
    "answer_1": "True",
    "question_2": "2. True or False: The frontend and the server tend to run together & the backend and the client tend to run together.",
    "answer_2": "False",
    "question_3": "3. True or False: The front end is NOT: JavaScript, HTML, CSS.",
    "answer_3": "False",
    "question_4": "4. True or False: Python controls all of its flow through indentation.",
    "answer_4": "True"}    

x=[]
def quiz_setup(x):
    """
    function that controls quiz setup
    """

    temp = x
    
    lect = temp.get("lecture")         #extract the lecture name from the list
    q1 = temp.get("question_1")        #extract question#1 from the list
    q2 = temp.get("question_2")        #extract question#2 from the list
    q3 = temp.get("question_3")        #extract question#3 from the list
    q4 = temp.get("question_4")        #extract question#4 from the list

    a = temp.get("answer_1")            #extract the answer for question#1 from the list
    b = temp.get("answer_2")            #extract the answer for question#2 from the list
    c = temp.get("answer_3")
    d = temp.get("answer_4")   

    return lect,q1,q2,q3,q4,a,b,c,d


