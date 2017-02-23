#String

#Basic String Operations  基本的String运算

#join, split, strip, upper(), lower()
>>> s = " this is  a  python course. \n"
>>> words = s.split()
>>> words
['this', 'is', 'a', 'python', 'course.']
>>> s.strip()  #s.strip(rm) 删除s字符串中开头、结尾处，位于 rm删除序列的字符 rm=None，默认删除空白符（包括'\n', '\r',  '\t',  ' ') 
'this is  a  python course.'
>>> " ".join(words)
'this is a python course.'
>>> "; ".join(words).split("; ")
['this', 'is', 'a', 'python', 'course.']
>>> s.upper()
' THIS IS  A  PYTHON COURSE. \n'

Basic Search/Replace in String    基本查询/替换 in String

>>> "this is a course".find("is")
2
>>> "this is a course".find("is a")
5
>>> "this is a course".find("is at")
-1
>>> "this is a course".replace("is", "was")
'thwas was a course'
>>> "this is a course".replace(" is", " was")
'this was a course'
>>> "this is a course".replace("was", "were")
'this is a course'

String Formatting     String输出格式

>>> print “%.2f%%” % 97.2363
97.24%
>>> s = '%s has %03d quote types.' % ("Python", 2)
>>> print s
Python has 002 quote types.

#list, tuple(元组), str; buffer, xrange, unicode
>>> lists = [[]] * 3
>>> lists
[[], [], []]
>>> lists[0].append(3)
>>> lists
[[3], [3], [3]]  #不要怪，因为这个引用嘛  	

#the tricky *   狡猾的 *  (我觉得能不用就不用好啦，万一搞不清挺坏事哒)

>>> [1, 2] * 3 
[1,2,1,2,1,2]

>>> [] * 3 
[]

>>> [[]] * 3
[[], [], []]

>>> a = [3]
>>> b = a * 3
>>> b
[3, 3, 3]

>>> a[0] = 4
>>> b
[3, 3, 3]

>>> a = [[3]] 
>>>b=a*3 
>>> b
[[3], [3], [3]]

>>> a[0][0] = 4
[[4], [4], [4]]

>>> a[0] = 5
>>> b
[[4], [4], [4]]

>>> a
>>> b = [a] * 3
>>> b
[[3], [3], [3]]

>>> a[0] = 4
>>> b
[[4], [4], [4]]

>>> b[1] = 5
>>> b
[[4], 5, [4]]

>>> b[0] += [2]
[[4, 2], 5, [4, 2]]

>>> " " * 3 ""
>>> "- " * 3 
"- - - "