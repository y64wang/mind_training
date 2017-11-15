#!/usr/bin/python

import sys, getopt
import random

MAXCOL = 5
MAXCOUNT = 100
MAXNUM = 100

def print_arithm():

  myops = [random.randint(0,1) for _ in range (MAXCOUNT)]

  for idx in range(MAXCOUNT):
    if myops[idx/2] == 0:
        sum = random.randint(21, MAXCOUNT - 1)
        x = random.randint(11, sum - 5)
        y = sum - x
        print "%2d "%x + "+" + " %2d"%y + " =\t\t",
    else:
        x = random.randint(11, MAXCOUNT - 1)
        y = random.randint(5, x - 1)
        print "%2d "%x + "-" + " %2d"%y + " =\t\t",

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
