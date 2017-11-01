#!/usr/bin/python
# lte codejame contest, author Wang Yong (10249631)

import sys, getopt

def FindMaxSatisfyGroup(info, groups):
    remainder = []
    for x in groups:
        remainder.append(x % info[1])
    remainder.sort()
    remCount = [remainder.count(0), remainder.count(1), \
                remainder.count(2), remainder.count(3)]    
    sumofOther = 0

    if info[1] == 2:
        numofOther = remCount[1] / 2
        if remCount[1] % 2 == 1:
            numofOther += 1

    elif info[1] == 3:
        numofOther = min(remCount[1], remCount[2])
        diff = abs(remCount[1] - remCount[2])
        numofOther  += diff / 3
        if not diff % 3  == 0:
            numofOther += 1
            
    elif info[1] == 4:
        numofOther = min(remCount[1], remCount[3])
        numofOther += remCount[2] / 2

        diff13 = abs(remCount[1] - remCount[3])
        diff2 = remCount[2] % 2

        if diff2 == 1 and diff13 >= 2:
            numofOther += 1
            diff2 -= 1
            diff13 -= 2
            
        numofOther += diff13 / 4
        if not diff13 % 4 == 0 or diff2 == 1:
            numofOther += 1

    return remCount[0] + numofOther

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print 'usage: Candy.py -i <inputfile>'
        sys.exit(2)
    optFound = False;
    for opt, arg in opts:
        if opt == '-h':
            print 'usage: Candy.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i"):
            inFileName = arg
            optFound = True;
    if not optFound:
        print 'usage: Candy.py -i <inputfile>'
        sys.exit(2)

    outFileName = inFileName + "_Output"
    with open(inFileName, 'r') as inFileHandle:
        with open(outFileName, 'w') as outFileHandle:
            numCases = int(inFileHandle.readline())
            for caseNo in range(numCases):
                info = map(int, inFileHandle.readline().split(' '))
                groups = map(int, inFileHandle.readline().split(' '))
                
                maxSatisifyGroup = FindMaxSatisfyGroup(info, groups)
                outFileHandle.write("Case #" + str(caseNo+1) + ": " + str(maxSatisifyGroup) +"\n")

if __name__ == "__main__":
  main(sys.argv[1:])
