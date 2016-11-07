#!/usr/bin/python

import sys, getopt
import random

def print_arithm(num):

  myrandoms = [random.randrange(0,num,1) for _ in range (120)]
  while myrandoms.count(0) >= 9:
    myrandoms = [random.randrange(0,num,1) for _ in range (120)]

  myops = [random.randint(0,1) for _ in range (60)]

  for idx in range(0, len(myrandoms), 2):
    x = myrandoms[idx]
    y = myrandoms[idx+1]
    if myops[idx/2] == 0:
      if  x + y > num:
        y = random.randint(0, num - x)
      print "%2d "%x + " +" + " %2d"%y + " =\t",
    else:
      if myrandoms[idx] < myrandoms[idx+1]:
        x = myrandoms[idx + 1]
        y = myrandoms[idx]
      print "%2d "%x + " -" + " %2d"%y + " =\t",

    if (idx/2 + 1)%3 == 0:
      print ""

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

  print_arithm(num)

if __name__ == "__main__":
  main(sys.argv[1:])
