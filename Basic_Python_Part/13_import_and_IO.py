#Basic import and I/O  import导入 和 I/O 基础

import sys  或者  from sys import *

#file copy
>>> f = open("my.in", "rt")  #f = open("my.in") 或者 f = open("my.in", "rt", encoding="utf-8") 有时候也行
>>> g = open("my.out", "wt") 
>>> for line in f:
...     print >> g, line,
... g.close()

#to read a line:
line = f.readline()

#to read all the lines:
lines = f.readlines()

#import and __main__

#demo  foo.py
def pp(a):
    print " ".join(a)
if __name__ == "__main__":   
	from sys import *
  	a = stdin.readline()
  	pp(a.split())

#import foo.py
import foo
>>>pp([[1, 2, 3]])
1 2 3





#over the basic part of python
##################################################################################