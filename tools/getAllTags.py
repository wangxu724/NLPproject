import nltk
import re
from nltk.tag import StanfordNERTagger
from random import randint
from sets import Set
import sys
sys.path.append('../')
from utility import load_data




def collectAllTags(qaTests):
    rlt = Set([])
    for i in range(len(qaTests)):
        test = qaTests[i]

        total = len(test.questions)
        for p in test.story_text:
            total = total + len(p)
        count = 1

        for q in test.questions:
            #ans = "Answer: " + try_NER_grammar(q[1], qaTest.story_text)
            words = nltk.word_tokenize(q[1])
            pos_words = nltk.pos_tag(words)
            for p in pos_words:
                rlt.add(p[1])

            print test.story_title + "  " + str(i+1) + '/' + str(len(qaTests)) + "  " + str(count) + "/" + str(total)
            count = count + 1

        for para in test.story_text:
            for sent in para:
                words = nltk.word_tokenize(sent)
                pos_words = nltk.pos_tag(words)
                for p in pos_words:
                    rlt.add(p[1])
                print test.story_title + "  " + str(i+1) + '/' + str(len(qaTests)) + "  " + str(count) + "/" + str(total)
                count = count + 1

    f = open('all_tags.txt','w')
    for t in rlt:
        f.write(t+'\n')
    f.close()
    print rlt
    return


def printAllTagInfo():
    f = open('all_tags.txt')
    allTags = []
    for l in f:
        allTags.append(l.rstrip())
    f.close()
    for t in allTags:
        print '-----------------'
        nltk.help.upenn_tagset(t)
        print ""



if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python getAllTags.py  <input file>"
        sys.exit(0)

    qaTests = load_data(sys.argv[1])
    collectAllTags(qaTests)
    
    #printAllTagInfo()




