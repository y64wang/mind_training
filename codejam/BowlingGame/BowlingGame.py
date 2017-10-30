#!/usr/bin/python

import sys, getopt
import random

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print 'usage: BowlingGame.py -i <inputfile>'
        sys.exit(2)
    optFound = False;
    for opt, arg in opts:
        if opt == '-h':
            print 'usage: BowlingGame.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i"):
            infile = arg
            optFound = True;
    if not optFound:
        print 'usage: BowlingGame.py -i <inputfile>'
        sys.exit(2)


if __name__ == "__main__":
  main(sys.argv[1:])
