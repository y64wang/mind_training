#!/usr/bin/python
# lte codejame contest, author Wang Yong (10249631)

import sys, getopt

MAXDIST = 999

def Dijkstra(start, distMap):
    nodeNum = len(distMap)
    shortPath = [MAXDIST for i in range(nodeNum)]
    visited = [False for i in range(nodeNum)]

    shortPath[start] = 0
    visited[start] = True

    for i in range(nodeNum -1):
        minDist = MAXDIST
        foundNode = start
        for node in range(nodeNum):
            if visited[node] == False and not distMap[start][node] == MAXDIST:
                if minDist > distMap[start][node]:
                    minDist = distMap[start][node]
                    foundNode = node

        shortPath[foundNode] = minDist
        visited[foundNode] = True

        for node in range(nodeNum):
            if visited[node] == False and not distMap[foundNode][node] == MAXDIST:
                sumDist = minDist + distMap[foundNode][node]
                if distMap[start][node] > sumDist:
                    distMap[start][node] = sumDist

    return shortPath

def CheckRoute(info, longMenMap):
    result = "NO"

    L_Pos = Z_Pos = 0

    for i in range(info[1]):
        L_Idx = [ j for j,x in enumerate(longMenMap[i]) if x== 'L' ]
        if not L_Idx == []:
            L_Pos = i * info[0] + L_Idx[0]
            break;

    for i in range(info[1]):
        Z_Idx = [ j for j,x in enumerate(longMenMap[i]) if x== 'Z' ]
        if not Z_Idx == []:
            Z_Pos = i * info[0] + Z_Idx[0]
            break;

    if L_Idx == []  or Z_Idx == []:
        return result

    nodeNum = info[0] * info[1]
    distMap = [([] * nodeNum) for i in range(nodeNum) ]
    for n in range(nodeNum):
        src_x = n / info[0]
        src_y = n % info[0]
        src = longMenMap[src_x][src_y]
        for m in range(nodeNum):
            dest_x = m / info[0]
            dest_y = m % info[0]
            dest = longMenMap[dest_x][dest_y]
            if src_x == dest_x and src_y == dest_y:
                if src == '*':
                    distMap[n].append(MAXDIST)
                else:
                    distMap[n].append(0)
            elif (src_x == dest_x and abs(src_y - dest_y) == 1) or  \
                 (src_y == dest_y and abs(src_x - dest_x) == 1):
                if src == '*' or dest == '*':
                    distMap[n].append(MAXDIST)
                else:
                    distMap[n].append(1)
            else:
                distMap[n].append(MAXDIST)

    shortPath = Dijkstra(Z_Pos, distMap)

    if shortPath[L_Pos] > info[2]:
        result = "NO"
    else:
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
                info = map(int, info)
                longMenMap = []
                for i in range(info[1]):
                    line = inFileHandle.readline().strip('\n')
                    line = line.split(' ')
                    longMenMap.append(line)
                res = CheckRoute(info, longMenMap)
                outFileHandle.write("Case #" + str(caseNo+1) + ": " + res + "\n")

if __name__ == "__main__":
  main(sys.argv[1:])
