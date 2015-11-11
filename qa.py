from utility import load_data
from solver import QASolver
import sys
from random import randint















if __name__ == '__main__':
    if len(sys.argv) != 2:
        print "Usage: python qa.py <input file>"
        sys.exit(0)

    qaTests = load_data(sys.argv[1])

    rlt = []
    for qa in qaTests:
        rlt = rlt + QASolver(qa)
        break


    f = open('output.txt', 'w')
    for r in rlt:
        f.write(r[0]+'\n')
        f.write(r[1]+'\n')
        f.write("\n")
    f.close()



