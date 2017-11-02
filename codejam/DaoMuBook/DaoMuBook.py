#!/usr/bin/python
# lte codejame contest, author Wang Yong (10249631)

import sys, getopt

MAXPRICE = 9999

def FindMinPositiveNum(list):
    minval = MAXPRICE
    for x in list:
        if minval > x and not x==0:
            minval = x
    return minval

def CalculatePrice(combineNum):
    price =  combineNum[0] * 8 + combineNum[1] * 2 * 7.6 +  \
                 combineNum[2] * 3 * 7.2 + combineNum[3] * 4 * 6.4 +  \
                 combineNum[4] * 5 * 6
    return price

def FindBestCombine(leftBooks):
    combineNum = [0 for i in range(5)]
    combineNum[4] = min(leftBooks)
    leftBooks = [i - combineNum[4] for i in leftBooks]

    numof0 = leftBooks.count(0)
    while numof0 < 5:
        combineNum[4-numof0] = FindMinPositiveNum(leftBooks)
        for i,x in enumerate(leftBooks):
            if not x == 0:
                leftBooks[i] = x - combineNum[4-numof0]
        numof0 = leftBooks.count(0)

    minval = min( combineNum[2], combineNum[4])
    if not minval == 0:
        combineNum[2] -= minval
        combineNum[4] -= minval
        combineNum[3] += minval * 2

    bestPrice = CalculatePrice(combineNum)
    return bestPrice


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
            outFileHandle.write(str(numCases)+ "\n")
            for caseNo in range(numCases):
                line = inFileHandle.readline()
                leftBooks = [line.count("1"), line.count("2"), line.count("3"),   \
                             line.count("4"), line.count("5")]
                bestPrice = FindBestCombine(leftBooks)

                outFileHandle.write(("%.1f" % bestPrice).rstrip('0').rstrip('.') + "\n")

if __name__ == "__main__":
  main(sys.argv[1:])
