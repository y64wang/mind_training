#!/usr/bin/python

import sys, getopt
import random

def print_arithm(num):

  myrandoms = [random.randrange(0,num,1) for _ in range (120)]
  myops = [random.randint(0,1) for _ in range (60)]

  #myarithm = (map(lambda idx: "%d "%myrandoms[idx] + ("+" if myops[idx/2]==0 else "-") + " %d"%myrandoms[idx+1], range(0, len(myrandoms), 2)))
  for idx in range(0, len(myrandoms), 2):
    if myops[idx/2] == 0:
      print "%d "%myrandoms[idx] + "+" + " %d"%myrandoms[idx+1] + " =\t\t",
    else:
      if myrandoms[idx] >= myrandoms[idx+1]:
        x = myrandoms[idx]
        y = myrandoms[idx+1]
      else:
        x = myrandoms[idx+1]
        y = myrandoms[idx]

      print "%d "%x + "-" + " %d"%y + " =\t\t",

    if (idx/2 + 1)%3 == 0:
      print ""



  #print "\n\n".join(map(lambda idx:'\t'.join(map(lambda item: '%02d'%item if (not skip) or (item != skip_num) else "  ", its[idx:idx+num])), range(0, len(its), num)))


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
