#!/bin/python

import sys

g = int(raw_input().strip())
for g0 in xrange(g):
  n = int(raw_input().strip())

  d = dict() ; j=0
  for i in raw_input().strip().split(' '):
    d[int(i)] = j ; j+=1

  import collections
  od = collections.OrderedDict(sorted(d.items(), reverse=True))

  AB = 0 ; i = n
  for val, idx in od.iteritems():
    if idx < i:
      i = idx
      AB = 1 - AB

  print 'ANDY' if AB==0 else 'BOB'
