import sys
import os





class QATest:
    def __init__(self, name):
        #name is the file name
        #story_title is a string
        #story_date is a string
        #story_id is a string
        #story_text is a list of paragraph, where paragraph is a list of sentence(string)
        #questions is a list of (questionID, question, difficulty)
        #answers is a list of (answerID, question, answer, difficulty)
        self.name = name
        self.story_title = None
        self.story_date = None
        self.story_id = None
        self.story_text = None
        self.questions = None
        self.answers = None



def load_data(filename):
    f = open(filename)
    IDs = []
    directory = f.readline().rstrip()
    while len(directory) > 0 and directory[-1] == '/':
        directory = directory[:-1]
    while True:
        l = f.readline()
        if l == "":
            break
        l = l.rstrip()
        if l != "":
            IDs.append(l.rstrip())
    f.close()
    rlt = []
    for i in IDs:
        qa = QATest(i)
        tmp = read_story(directory+'/'+i+'.story')
        qa.story_title = tmp[0]
        qa.story_date = tmp[1]
        qa.story_id = tmp[2]
        qa.story_text = tmp[3]
        qa.questions = read_questions(directory+'/'+i+'.questions')
        qa.answers = read_answers(directory+'/'+i+'.answers')
        rlt.append(qa)
    return rlt



def read_story(filename):
    #return [title, date, id, text], where text is list of paragraph, where paragraph is a list of sentence
    title = ""
    date = ""
    sid = ""
    text = []
    i = 0
    f = open(filename)
    while True:
        l = f.readline()
        if l == "":
            break
        l = l.rstrip()
        if l == "TEXT:":
            break
        if not (l == "\n" or l == ""):
            tmp = l.split(':')
            if len(tmp) == 2 and tmp[0] == "HEADLINE":
                title = tmp[1].lstrip()
            elif len(tmp) == 2 and tmp[0] == "DATE":
                date = tmp[1].lstrip()
            elif len(tmp) == 2 and tmp[0] == "STORYID":
                sid = tmp[1].lstrip()

    buf = []
    while True:
        l = f.readline()
        if l == "":
            break
        l = l.rstrip()
        if len(buf) == 0:
            buf.append(l)
        else:
            if buf[-1] != "" and l != "":
                buf[-1] = buf[-1]+l
            else:
                buf.append(l)
    text = [[s for s in p.split('.') if s != ""] for p in buf if p != ""]
    f.close()
    return [title, date, sid, text]



def read_questions(filename):
    #return list of (questionID, question, difficulty)
    f = open(filename)
    rlt = []
    while True:
        l = f.readline()
        if l == "":
            break
        while l == '\n':
            l = f.readline()
        if l == "":
            break
        qid = l.split(':')[1].lstrip().rstrip()
        l = f.readline()
        q = l.split(':')[1].lstrip().rstrip()
        l = f.readline()
        d = l.split(':')[1].lstrip().rstrip().lower()
        rlt.append((qid, q, d))
    f.close()
    return rlt



def read_answers(filename):
    #return list of (answerID, question, answer, difficulty)
    f = open(filename)
    rlt = []
    while True:
        l = f.readline()
        if l == "":
            break
        while l == '\n':
            l = f.readline()
        if l == "":
            break
        qid = l.split(':')[1].lstrip().rstrip()
        l = f.readline()
        q = l.split(':')[1].lstrip().rstrip()
        l = f.readline()
        a = l.split(':')[1].lstrip().rstrip()
        l = f.readline()
        d = l.split(':')[1].lstrip().rstrip().lower()
        rlt.append((qid, q, a, d))
    f.close()
    return rlt










if __name__ == '__main__':
    pass 












