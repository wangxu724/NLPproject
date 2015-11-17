import nltk
import re
from nltk.tag import StanfordNERTagger
from random import randint
from sets import Set
import sys
sys.path.append('../')
from utility import load_data



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
        print "Usage: python showTagsInfo.py  <input file>"
        sys.exit(0)

    printAllTagInfo()




