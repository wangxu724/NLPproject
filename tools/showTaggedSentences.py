import nltk
import re
from nltk.tag import StanfordNERTagger
from random import randint
from sets import Set
import sys
sys.path.append('../')
from utility import load_data







def showAllTaggedSentences(qaTests):
    for qa in qaTests:
        for q in qa.questions:
            w = nltk.word_tokenize(q[1])
            posw = nltk.pos_tag(w)
            printPOS(posw)
        for para in qa.story_text:
            for s in para:
                w = nltk.word_tokenize(s)
                posw = nltk.pos_tag(w)
                printPOS(posw)

def printPOS(pos_words):
    #pos_words is a list of (word, tag)
    s = ""
    t = ""
    for p in pos_words:
        l = len(p[0]) if len(p[0]) > len(p[1]) else len(p[1])
        s = s + p[0].rjust(l) + ' '
        t = t + p[1].rjust(l) + ' '

    print '-----------'
    print s
    print t
    print ""





if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python showTaggedSentences.py <input file>"
        sys.exit(0)

    qaTests = load_data(sys.argv[1])

    showAllTaggedSentences(qaTests)



