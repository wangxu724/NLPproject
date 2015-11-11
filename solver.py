import nltk
from random import randint

def QASolver(qaTest):
    #return list of (questionID, answer)
    #where questionID = "QuestionID: xxxxxx", 
    #answer = "Answer: xxxxxxx"
    if len(qaTest.story_text) == 0:
        return []
    
    rlt = []
    for q in qaTest.questions:
        qid = "QuestionID: " + q[0]
        ans = "Answer: " + questionSolver(q[1], qaTest.story_text)
        rlt.append((qid, ans))
    return rlt



def questionSolver(question, story):
    #question is a string
    #story is the story_text in QATest
    words = nltk.word_tokenize(question)
    pos_words =  nltk.pos_tag(words)
    parser = nltk.parse.malt.MaltParser()
    for tree in parser.parse(pos_words):
        print(tree)




    return str(randint(0,100))





















