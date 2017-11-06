#!/usr/bin/python

import sys, getopt
import random

MAXCOL = 5
MAXCOUNT = 100
MAXNUM = 100

def print_arithm(num):

  myrandoms = [random.randrange(1,num,1) for _ in range (2*MAXCOUNT)]

  myops = [random.randint(0,1) for _ in range (MAXCOUNT)]

  for idx in range(0, len(myrandoms), 2):
    x = myrandoms[idx]
    y = myrandoms[idx+1]
    if myops[idx/2] == 0:
      if  x + y > num:
        y = random.randint(1, num - x)
      print "%2d "%x + " +" + " %2d"%y + " =\t",
    else:
      if myrandoms[idx] < myrandoms[idx+1]:
        x = myrandoms[idx + 1]
        y = myrandoms[idx]
      print "%2d "%x + " -" + " %2d"%y + " =\t",

    if (idx/2 + 1)%MAXCOL == 0:
      print ""

  print""


def main(argv):
  num = MAXNUM
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

  print_arithm(num)

if __name__ == "__main__":
  main(sys.argv[1:])
