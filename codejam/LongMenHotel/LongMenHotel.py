#!/usr/bin/python
# lte codejame contest, author Wang Yong (10249631)

import sys, getopt

def CheckCatchup(info, longMenMap):
    result = "YES"

    return result

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print 'usage: LongMenHotel.py -i <inputfile>'
        sys.exit(2)
    optFound = False;
    for opt, arg in opts:
        if opt == '-h':
            print 'usage: LongMenHotel.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i"):
            inFileName = arg
            optFound = True;
    if not optFound:
        print 'usage: LongMenHotel.py -i <inputfile>'
        sys.exit(2)

    outFileName = inFileName + "_Output"
    with open(inFileName, 'r') as inFileHandle:
        with open(outFileName, 'w') as outFileHandle:
            numCases = int(inFileHandle.readline())
            for caseNo in range(numCases):
                info = inFileHandle.readline().split(' ')
                longMenMap = []
                for i in range(int(info[1])):
                    line = inFileHandle.readline().split(' ')
                    longMenMap.append(line)
                print info[0] + " " + info[1] + " " + info[2]
                print longMenMap[0][0]
                #outFileHandle.write(result + "\n")

if __name__ == "__main__":
  main(sys.argv[1:])
