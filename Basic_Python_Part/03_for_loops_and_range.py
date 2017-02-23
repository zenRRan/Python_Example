#for loops and range()

>>> sum = 0
>>> for i in range(10): 
... sum+=i
...
>>> print sum
45
>>> for word in ["welcome", "to", "python"]: 
... print word,
...
welcome to python

>>> range(5), range(4,6), range(1,7,2)
([0, 1, 2, 3, 4], [4, 5], [1, 3, 5])


#while loops

>>> while b <= 5:
       print b
       a, b = b, a+b
1
1
2
3
5