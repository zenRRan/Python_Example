#Conditionals  条件

 >>> if x < 10 and x >= 0:
...      print x, "is a digit" 
...
>>> False and False or True True
>>> not True
False

>>> if 4 > 5:
... print "foo" 
... else:
... print "bar" 
...
bar

 >>> print “foo” if 4 > 5 else “bar”
...
>>> bar

>>> a = "foo"
>>> if a in ["blue", "yellow", "red"]:
... print a + " is a color"
... else:
...    if a in ["US", "China"]:
...     printa+"isacountry"
...   else:
...        print "I don't know what”, a, “is!" 
...