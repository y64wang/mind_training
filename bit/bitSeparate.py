#!/usr/bin/python

import sys, getopt

def extract32(x):
    odd  = x& 0x55555555; #restrict to odd bits.
    odd = (odd | (odd >> 1)) & 0x33333333;
    odd = (odd | (odd >> 2)) & 0x0f0f0f0f;
    odd = (odd | (odd >> 4)) & 0x00ff00ff;
    odd = (odd | (odd >> 8)) & 0x0000ffff;

    even = (x << 1) & 0x55555555; #restrict to even bits.
    even = (even | (even >> 1)) & 0x33333333;
    even = (even | (even >> 2)) & 0x0f0f0f0f;
    even = (even | (even >> 4)) & 0x00ff00ff;
    even = (even | (even >> 8)) & 0x0000ffff;
    return even, odd

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

  print "input: %d " % num + " bin: {:032b}".format(num)
  even, odd = extract32(num)

  print "even : {:016b}".format(even)
  print "odd  : {:016b}".format(odd)


if __name__ == "__main__":
  main(sys.argv[1:])
