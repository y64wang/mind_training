#!/usr/bin/python
# lte codejame contest, author Wang Yong (10249631)

import sys, getopt

def CheckRoute(info, longMenMap):
    result = "YES"

    for i in range(int(info[1])):
        L_Idx = [ j for j,x in enumerate(longMenMap[i]) if x == 'L' ]
        if not L_Idx == []:
            L_Idx.insert(0, i)
            break

    for i in range(int(info[1])):
        Z_Idx = [ j for j,x in enumerate(longMenMap[i]) if x == 'Z' ]
        if not Z_Idx == []:
            Z_Idx.insert(0, i)
            break

    print L_Idx
    print Z_Idx

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
                    line = inFileHandle.readline().strip('\n')
                    line = line.split(' ')
                    longMenMap.append(line)
                CheckRoute(info, longMenMap)
                #outFileHandle.write(result + "\n")

if __name__ == "__main__":
  main(sys.argv[1:])
