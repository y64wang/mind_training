#!/usr/bin/python

import sys, getopt

def count32(num):
    num = num - ((num >> 1) & 0x55555555)
    num = (num & 0x33333333) + ((num >>2) & 0x33333333)
    num = (((num + (num >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24
    return num

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
  count = count32(num)

  print "bit count: %d" % count


if __name__ == "__main__":
  main(sys.argv[1:])
