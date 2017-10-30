#!/usr/bin/python

import sys, getopt

def TransScore(frame):
    scores = []
    if frame[0] == 'X':
        scores.append(10)
    elif frame[0] == '-':
        scores.append(0)
    else:
        scores.append(int(frame[0]))


    if len(frame) > 1:
        if frame[1] == 'X':
            scores.append(10)
        elif frame[1] == '/':
            scores.append(10-scores[0])
        elif frame[1] in ['-', '\n']:
            scores.append(0)
        else:
            scores.append(int(frame[1]))

    return scores

def CalculateBowlingGameScore(game):
    frames = game.split('|')
    if len(frames) > 10:
        frames[10] = frames[11]

    balls = []
    for frame in frames:
        balls.extend(TransScore(frame))

    totalScore = 0
    idx = 0
    for frame in frames[0:10]:
        if frame[0] == 'X':
            totalScore += (balls[idx] + balls[idx + 1] + balls[idx + 2])
            idx += 1
        elif len(frame) > 1:
            if frame[1] == '/':
                totalScore += (balls[idx] + balls[idx + 1] + balls[idx + 2])
                idx += 2
            else:
                totalScore += (balls[idx] + balls[idx + 1])
                idx += 2

    return totalScore

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
            inFileName = arg
            optFound = True;
    if not optFound:
        print 'usage: BowlingGame.py -i <inputfile>'
        sys.exit(2)

    outFileName = inFileName + "_Output"
    with open(inFileName, 'r') as inFileHandle:
        with open(outFileName, 'w') as outFileHandle:
            numGames = int(inFileHandle.readline())
            for line in range(numGames):
                curGame = inFileHandle.readline();
                score = CalculateBowlingGameScore(curGame)
                outFileHandle.write(str(score) + '\n')

if __name__ == "__main__":
  main(sys.argv[1:])
