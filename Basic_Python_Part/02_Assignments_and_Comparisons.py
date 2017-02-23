#Assignments and Comparisons  作业和比较练习

>>> a = b = 0
>>> a
0
>>> b
0
>>> a, b = 3, 5
>>> a + b
8
>>> (a, b) = (3, 5)
>>> a + b
>>> 8
>>> a, b = b, a
(swap)  #交换

>>> a = b = 0
>>> a == b
True
>>> type (3 == 5)
<type 'bool'>
>>> "my" == 'my'
True
>>> (1, 2) == (1, 2)
True
>>> 1, 2 == 1, 2
(1, False, 2)