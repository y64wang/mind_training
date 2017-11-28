#!/usr/bin/python

import sys, getopt
import random

MAXCOL = 5
MAXCOUNT = 100
MAXNUM = 100
MUL_ENABLED = 1

def print_arithm():

  for idx in range(MAXCOUNT):
    ops = random.randint(0, 1 + MUL_ENABLED)
    if ops == 0:
        sum = random.randint(21, MAXNUM - 1)
        x = random.randint(11, sum - 5)
        y = sum - x
        print "%3d "%x + "+" + " %3d"%y + " =\t\t",
    elif ops == 1:
        x = random.randint(11, MAXNUM - 1)
        y = random.randint(5, x - 1)
        print "%3d "%x + "-" + " %3d"%y + " =\t\t",
    else:
        x = random.randint(1, 9)
        y = random.randint(1, 9)
        print "%3d "%x + "x" + " %3d"%y + " =\t\t",

    if (idx + 1)%MAXCOL == 0:
      print ""

  print""
  print""


def main(argv):
  num = 10
  try:
    opts, args = getopt.getopt(argv,"hn:")
  except getopt.GetoptError:
    print 'usage: arithmetic.py -n <num>'
    sys.exit(2)
  for opt, arg in opts:
    if opt == '-h':
      print 'usage: arithmetic.py -n <num>'
      sys.exit()
    elif opt in ("-n"):
      num = int(arg)

  for x in range(num):
    print_arithm()
    #if (x+1)%2 == 0:
    #    print "\f"

if __name__ == "__main__":
  main(sys.argv[1:])
