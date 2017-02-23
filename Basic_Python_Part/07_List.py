#Basic List Operations 基本的List运算

#length, subscript, and slicing 长度 字段 和 截取

>>> a = [1,'python', [2,'4']]  #List包括各种类型
>>> len(a)
3
>>> a[2][1]
'4'
>>> a[3]
IndexError!
>>> a[-2]  #倒数第二个   a[-1]最后一个  a[-0] 表示第一个 和a[0] 一样
'python'
#a[:]
>>> a[1:2]  #a[开始:结束(不包括)] 截取的仍然为List
['python']

#a[A:B:C]  A > B && C > 0 表示 从第A个开始到B每隔C个数的所有数    A < B && C < 0  表示  从第A个开始到B每隔绝对值C个数的所有数  
>>> a[0:3:2]
[1, [2, '4']]
>>> a[:-1]
[1, 'python']
>>> a[0:3:]
[1, 'python', [2, '4']]
>>> a[0::2]
[1, [2, '4']]
>>> a[::]
[1, 'python', [2, '4']]
>>> a[:]
[1, 'python', [2, '4']]

##################################################################
+, extend, +=, append

 >>> a = [1,'python', [2,'4']]
>>> a + [2]
[1, 'python', [2, '4'], 2]
>>> a.extend([2, 3])
>>> a
[1, 'python', [2, '4'], 2, 3]
same as a += [2, 3]
>>> a.append('5')
>>> a
[1, 'python', [2, '4'], 2, 3, '5']
>>> a[2].append('xtra')
>>> a
[1, 'python', [2, '4', 'xtra'], 2, 3, '5']

##################################################################
Comparison and Reference 比较和引用 (记住是引用)  (Ture and False)

>>> [1, '2'] == [1, '2']
True
>>> a = b = [1, '2']
>>> a == b
True
>>> a is b 
True
>>> b [1] = 5 
>>> a
[1, 5]
>>> a = 4
>>> b
[1, 5]
>>> a is b 
False

>>> c = b [:]
>>> c
[1, 5]
>>> c == b
True 
>>> c is b
False

>>> b[:0] = [2]
>>> b
[2, 1, 5]
>>> b[1:3]=[]
>>> b
[2]
>>> a = b
>>> b += [1]
>>> a is b 
True
####   a += b means a.extend(b)， NOT  a = a + b !!

####################################################################
List Comprehension List理解

>>> a = [1, 5, 2, 3, 4 , 6]
>>> [x*2 for x in a]
[2, 10, 4, 6, 8, 12]

>>> [x for x in a if \
... len( [y for y in a if y < x] ) == 3 ]  
[4]
#######
# for x in a :
# 	for y in a :
# 		if y < x 的个数等于三 的x的集合


>>> a = range(2,10)   # a = [2,3,4,5,...9]
>>> [x*x for x in a if \
... [y for y in a if y < x and (x % y == 0)] == [] ] #square of prime numbers 素数的平方
[4, 9, 25, 49]

>>> vec = [2, 4, 6]
>>> [[x,x**2] for x in vec]
[[2, 4], [4, 16], [6, 36]]
>>> [x, x**2 for x in vec]
SyntaxError: invalid syntax
>>> [(x, x**2) for x in vec]
[(2, 4), (4, 16), (6, 36)]

>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [x*y for x in vec1 for y in vec2]
[8, 6, -18, 16, 12, -36, 24, 18, -54]
>>> [x+y for x in vec1 for y in vec2]
#(cross product)
[6, 5, -7, 8, 7, -5, 10, 9, -3]
#should use zip instead!
>>> [vec1[i]*vec2[i] for i in range(len(vec1))]
[8, 12, -54]