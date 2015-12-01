import nltk
import re
from sets import Set
from nltk.tag import StanfordNERTagger
from nltk.stem import SnowballStemmer
from random import randint

def QASolver(qaTest):
    #return list of (questionID, answer)
    #where questionID = "QuestionID: xxxxxx", 
    #answer = "Answer: xxxxxxx"
    if len(qaTest.story_text) == 0:
        return []
    
    rlt = []
    # pos_parse each sentences
    # story_pos = sentencesParse(qaTest.story_text)
    for q in qaTest.questions:
        qid = "QuestionID: " + q[0]
        ans = "Answer: " + questionSolver(q[1], qaTest.story_text)
        rlt.append((qid, ans))
    return rlt


def sentencesParse(story):
    pos_sent = []
    print story
    for para in story:
        print "PARA:"
        print para
        para_sent = []
        for sent in para:
            print "SENTENCE:"
            print sent
            words = nltk.word_tokenize(sent)
            pos_words =  nltk.pos_tag(words)
            para_sent.append(pos_words)
        pos_sent.append(para_sent)
    return pos_sent

def back_a_step(story, i, j):
    if j > 0:
        return i, j - 1;
    elif j == 0:
        if i == 0:
            return i, j;
        elif i > 0:
            return i - 1, len(story[i]) - 1;

def isNNP(item):
    return item == 'NNP' or item == 'NN' or item == 'NNS'

def isADJ(item):
    return item == 'DT' or item == 'IN' or item == 'CC' or item == 'JJ'

# The stop words is not good
def getStopWordSet():
    stopword = Set(["a", "an", "the", "he", "she", "it", "they", "them", "those", "their", "these", "of", "to", "from", "by", "with", "for", "at", "should", "would", "could", "can", "will", "must", "shall"])
    # stopword = Set([])
    return stopword

def getStem(word):
    stemmer = SnowballStemmer("english")
    return stemmer.stem(word)

def getQuesWords():
    key_words = Set(["what", "where", "when", "why", "how", "who", "which", "whose", "whom"])
    return key_words

def getQuesKeyWords(ques_words, ques_key_words):
    i = 0
    for word in ques_words:
        temp = word.lower() 
        if temp in ques_key_words:
            if word[0] >= 'a' and word[0] <= 'z':
                word = str(word[0]).upper() + word[1:]
            return (word, i + 1)
        i += 1
    return ("", 0)

def deleteDuplicateWord(question, sentence):
    ans = ""
    for word in sentence:
        if word not in question:
            ans = ans + word + " "
    return ans


def questionSolver(question, story):
    #question is a string
    #story is the story_text in qaTest
    
    # Ensure the type of answer from what, when, who, etc.
    # ans_types = {'person', 'location', 'object', 'number', 'time', 'pattern', 'reason'};
    stopword = getStopWordSet()

    # Parse the Quesiton
    ques_words = question.split(" ");

    # Get keyword from question
    # Where, What, When, Why, Who, How
    ques_key_words = getQuesWords()

    (key_word, nextID) = getQuesKeyWords(ques_words, ques_key_words)
    key_map = {"many": 0, "much": 0, "long": 0, "old": 0, "far": 0}
    isnumber = False
    
    ###################################
    ### Print The key Word of Question
    ###################################
    print key_word

    if key_word == "How":
        if ques_words[nextID] in key_map:
            print ques_words[nextID]
            isnumber = True;

    # print ques_words;
    for i in range(len(ques_words)):
        ques_words[i] = ques_words[i].replace('?', '')
        ques_words[i] = ques_words[i].lower()
        ques_words[i] = getStem(ques_words[i])
    
    ques_words_set = set(ques_words[:]);
    # print ques_words_set

    i = 0
    j = 0
    maxi = 0
    maxj = 0
    maxcount = 0;
    for para in story:
        for sent in para:
            j = 0
            count = 0;
            sent_word = sent.split(' ');
            for word in sent_word:
                if word.isalpha() == False:
                    word = re.sub('[^A-Za-z]', '', word)
                word = word.lower()
                word = getStem(word)
                if word not in stopword and word in ques_words_set:
                    count += 1;
            if count >= maxcount:
                maxcount = count
                maxi = i
                maxj = j
            j += 1;
        i += 1;

    res_sent = []
    for para in story:
        for sent in para:
            j = 0
            count = 0;
            sent_word = sent.split(' ');
            for word in sent_word:
                if word.isalpha() == False:
                    word = re.sub('[^A-Za-z]', '', word)
                word = word.lower()
                word = getStem(word)
                if word not in stopword and word in ques_words_set:
                    count += 1;
            if count == maxcount:
               res_sent.append(sent);
            j += 1;
        i += 1;

    if key_word == "Why": 
        return res_sent[0]
    elif key_word == "Who" or key_word == "Whom" or key_word == "Whose" or key_word == "Which":

        for sent in res_sent:
            pos_sents = nltk.pos_tag(nltk.word_tokenize(sent));

            item_word = ""
            flag = False;
            for item in pos_sents:
                if isNNP(item[1]) or isADJ(item[1]):
                    if flag == True:
                        item_word = ""
                    temp = re.sub('[^A-Za-z]', '', item[0].lower());
                    if temp in ques_words_set:
                        if isNNP(item[1]):
                            flag = True;
                        else:
                            if item_word != "":
                                return item_word
                    else:
                        item_word += item[0] + ' ';
                elif isNNP(item[1]) == False and isADJ(item[1]):
                    if flag == True:
                        item_word = ""
                    flag = False
                    if item_word != "":
                        return item_word



    elif key_word == "What":
        for sent in res_sent:
            pos_sents = nltk.pos_tag(nltk.word_tokenize(sent));

            nnp_words = []
            item_word = ""
            flag = False;
            for item in pos_sents:
                if isNNP(item[1]) or item[1] == 'JJ':
                    if flag == True:
                        item_word = ""
                        continue
                    temp = re.sub('[^A-Za-z]', '', item[0]).lower();
                    if isNNP(item[1]) and temp in ques_words_set:
                        flag = True
                    else:
                        item_word += item[0] + " ";
                else:
                    flag = False
                    if item_word != "":
                        # nnp_words.append(item_word)
                        return item_word;
                        item_word = ""
    elif key_word == "When" or key_word == "Where":
        for sent in res_sent:
            pos_sents = nltk.pos_tag(nltk.word_tokenize(sent));
            item_word = ""
            in_flag = False;
            flag = False;
            for item in pos_sents:
                if item[1] == "IN" and (item[0] == 'in' or item[0] == 'on' or item[0] == 'at'):
                    in_flag = True;
                    flag = False;
                elif in_flag == True and (item[1] == 'DT' or isNNP(item[1]) or item[1] == 'IN' or item[1] == 'CC' or item[1] == 'JJ'):
                    if flag == True:
                        item_word = ""
                        continue
                    temp = re.sub('[^A-Za-z]', '', item[0]).lower();
                    if item[1] == 'NNP' and temp in ques_words_set:
                        flag = True
                    else:
                        item_word += item[0] + " ";
                else:
                    flag = False
                    if item_word != "" and in_flag == True:
                        return item_word;
    elif key_word == "How":
        for sent in res_sent:
            pos_sents = nltk.pos_tag(nltk.word_tokenize(sent));
            if isnumber == True:
                for item in pos_sents:
                    if item[1] == "CD":
                        return item[0];
        return res_sent[0]
    else:
        print question
        return story[maxi][maxj]



    if item_word != "":
        return item_word
    return story[maxi][maxj]





















