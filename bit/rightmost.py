#!/usr/bin/python

import sys, getopt

MUL_DE_BRUIJN_BIT =  \
[0, 1, 28, 2, 29, 14, 24, 3, 30, 22, 20, 15, 25, 17, 4, 8, \
  31, 27, 13, 23, 21, 19, 16, 7, 26, 12, 18, 6, 11, 5, 10, 9]

def print_help():
    print 'usage: bitscan.py -n <num>'
    sys.exit(2)

def main(argv):
  num = 0
  try:
    opts, args = getopt.getopt(argv,"hn:")
  except getopt.GetoptError:
    print_help()
  optFound = False
  for opt, arg in opts:
    if opt == '-h':
      print_help()
    elif opt in ("-n"):
      num = int(arg)
      optFound = True

  if not optFound:
      print_help()

  print "input: %d " % num + " bin: {0:b}".format(num)

  num = num & ~(num - 1)

  print "right most bit: " + "{0:b}".format(num)

  index = MUL_DE_BRUIJN_BIT[((num * 0x077CB531) & 0xFFFFFFFF) >> 27]
  print "bit index: %d" % index


if __name__ == "__main__":
  main(sys.argv[1:])
