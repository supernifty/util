
from optparse import OptionParser

parser = OptionParser()
options, args = parser.parse_args()

for arg in args:
  fd = open( arg, 'rU' )
  row = 1
  for line in fd:
    for c in line:
      column = 1
      if ord(c) > 127:
        print "%s: line %i column %i" % ( arg, row, column )
        column += 1
    row += 1

