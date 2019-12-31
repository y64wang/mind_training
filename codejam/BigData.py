#!/usr/bin/python
# lte codejame contest, author Wang Yong (10249631)

import sys, getopt

def CompareAbsoluteNum(num1, num2):
    result = 1
    if len(num1) > len(num2):
        result = 1
    elif len(num1) < len(num2):
        result = -1
    else:
        resultFound = False
        for i in range(len(num1)):
            if int(num1[i]) > int(num2[i]):
                result = 1
                resultFound = True
                break
            elif int(num1[i]) < int(num2[i]):
                result = -1
                resultFound = True
                break
        if resultFound == False:
            result = 0

    return result

def AbsoluteAdd(num1, num2):
    revNum1 = num1[::-1]
    revNum2 = num2[::-1]
    if len(num1) > len(num2):
        longNum = revNum1
        shortNum = revNum2
    else:
        longNum = revNum2
        shortNum = revNum1

    result = ""
    carry = 0
    for i in range(len(shortNum)):
        curPos = int(shortNum[i]) + int(longNum[i]) + carry
        if curPos > 9:
            curPos -= 10
            carry = 1
        else:
            carry = 0
        result += str(curPos)

    for i in range(len(shortNum), len(longNum)):
        curPos = int(longNum[i]) + carry
        if curPos > 9:
            curPos -= 10
            carry = 1
        else:
            carry = 0
        result += str(curPos)
    if carry == 1:
        result += str(carry)

    result = result[::-1]
    return result 

def AbsoluteSub(num1, num2):
    revNum1 = num1[::-1]
    revNum2 = num2[::-1]
    
    result = ""
    carry = 0
    for i in range(len(revNum2)):
        curPos = int(revNum1[i]) - int(revNum2[i]) - carry
        if curPos < 0:
            curPos += 10
            carry = 1
        else:
            carry = 0
        result += str(curPos)

    for i in range(len(revNum2), len(revNum1)):
        curPos = int(revNum1[i]) - carry
        if curPos < 0:
            curPos += 10
            carry = 1
        else:
            carry = 0
        result += str(curPos)

    nPos = 0
    result = result[::-1]
    for i in range(len(result)):
        if not result[i] == '0':
            nPos = i
            break
    result = result[nPos::]
    return result


def BigDataAdd(num1, num2):
    sign = ""
    result = ""
    if num1[0] == '-' and num2[0] == '-':
        sign = "-"
        absNum1 = num1.strip('-')
        absNum2 = num2.strip('-')
        result = AbsoluteAdd(absNum1, absNum2)
    elif not num1[0] == '-' and  not num2[0] == '-':
        result = AbsoluteAdd(num1, num2)
    elif not num1[0] == '-' and num2[0] == '-':
        absNum2 = num2.strip('-')
        compareRes = CompareAbsoluteNum(num1, absNum2)
        if compareRes == 1:
            result = AbsoluteSub(num1, absNum2)
        elif compareRes == -1:
            result = AbsoluteSub(absNum2, num1)
            sign = "-"
        else:
            result = "0"
    elif num1[0] == '-' and not num2[0] == '-':
        absNum1 = num1.strip('-')
        compareRes = CompareAbsoluteNum(absNum1, num2)
        if compareRes == 1:
            result = AbsoluteSub(absNum1, num2)
            sign = "-"
        elif compareRes == -1:
            result = AbsoluteSub(num2, absNum1)
        else:
            result = "0"

    result = sign + result
    return result

def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hi:")
    except getopt.GetoptError:
        print 'usage: BigData.py -i <inputfile>'
        sys.exit(2)
    optFound = False;
    for opt, arg in opts:
        if opt == '-h':
            print 'usage: BigData.py -i <inputfile>'
            sys.exit()
        elif opt in ("-i"):
            inFileName = arg
            optFound = True;
    if not optFound:
        print 'usage: BigData.py -i <inputfile>'
        sys.exit(2)

    outFileName = inFileName + "_Output"
    with open(inFileName, 'r') as inFileHandle:
        with open(outFileName, 'w') as outFileHandle:
            for line in inFileHandle:
                line = line.strip('\n')
                numbers = line.split(',')
                result = BigDataAdd(numbers[0], numbers[1])
                outFileHandle.write(result + "\n")

if __name__ == "__main__":
  main(sys.argv[1:])
