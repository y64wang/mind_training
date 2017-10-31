#!/usr/bin/python
# lte codejame contest, author Wang Yong (10249631)

import sys, getopt


def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print 'usage: DaoMuBook.py -i <inputfile>'
        sys.exit(2)
    optFound = False;
    for opt, arg in opts:
        if opt == '-h':
            print 'usage: DaoMuBook.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i"):
            inFileName = arg
            optFound = True;
    if not optFound:
        print 'usage: DaoMuBook.py -i <inputfile>'
        sys.exit(2)

    outFileName = inFileName + "_Output"
    with open(inFileName, 'r') as inFileHandle:
        with open(outFileName, 'w') as outFileHandle:
            numCases = int(inFileHandle.readline())
            for caseNo in range(numCases):
                line = inFileHandle.readline()
                num1 = line.count("1")
                num2 = line.count("2")
                num3 = line.count("3")
                num4 = line.count("4")
                num5 = line.count("5")
                print "1: " + str(num1) + " 2: " + str(num2) + " 3: " + str(num3) + \
                        " 4: " + str(num4) + " 5: " + str(num5)
                #outFileHandle.write("Case #" + str(caseNo+1) + ": " + res + "\n") 

if __name__ == "__main__":
  main(sys.argv[1:])
