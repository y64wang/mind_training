#!/usr/bin/python

import sys, getopt
import random

def print_grid(num, skip):
  
  skip_num = random.randint(0, num*num-1)

  its = range(0, num*num)

  random.shuffle(its)

  print "\n\n".join(map(lambda idx:'\t'.join(map(lambda item: '%02d'%item if (not skip) or (item != skip_num) else "  ", its[idx:idx+num])), range(0, len(its), num)))


def main(argv):
   num = 6
   skip = False
   try:
      opts, args = getopt.getopt(argv,"hn:s")
   except getopt.GetoptError:
      print 'usage: schulte_table.py -n <num> -s'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'usage: schulte_table.py -n <num> -s'
         sys.exit()
      elif opt in ("-n"):
         num = int(arg)
      elif opt in ("-s"):
         skip = True

   print_grid(num, skip) 

if __name__ == "__main__":
   main(sys.argv[1:])
