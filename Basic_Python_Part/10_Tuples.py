#Python的元组与列表类似，不同之处在于元组的元素不能修改,元组使用小括号,
#列表使用方括号,元组创建很简单,只需要在括号中添加元素,并使用逗号隔开即可
Tuples  元组   <immutable lists>不变的lists

#Tuples and Equality   元组和等式

##caveat: singleton tuple 这里是单元组
a += (1,2)  # new copy
a += [1,2]  # in-place

>>> (1, 'a')
(1, 'a')
>>> (1)
1
>>> [1]
[1]
>>> (1,)
(1,)
>>> [1,]
[1]
>>> (5) + (6)
11
>>> (5,)+ (6,)
(5, 6)

#==,is,is not

>>> 1, 2 == 1, 2  #false是2 == 1 ,合起来是1，false，2   在控制台返回值是元组也就是下面的输出
(1, False, 2)
>>> (1, 2) == (1, 2)
True
>>> (1, 2) is (1, 2)
False
>>> "ab" is "ab"
True
>>> [1] is [1]
False
>>> 1 is 1
True
>>> True is True
True

#Comparison

##cmp(): three-way <, >, ==

>>> (1, 'ab') < (1, 'ac')
True
>>> (1, ) < (1, 'ac')
True
>>> [1] < [1, 'ac']
True
>>> 1 < True
False
>>> True < 1
False

>>> [1] < [1, 2] < [1, 3]
True
>>> [1] == [1,] == [1.0]
True
>>> cmp ( (1, ), (1, 2) )
-1
>>> cmp ( (1, ), (1, ) )
0
>>> cmp ( (1, 2), (1, ) )
1

#enumerate 枚举

>>> words = ['this', 'is', 'python']
>>> i = 0
>>> for word in words:
... i+=1
...     print i, word
...
1 this
2 is
3 python
>>> for i, word in enumerate(words):
...     print i+1, word
...

#zip and _   # _参与循环，但不获取值

>>> a = [1, 2]
>>> b = ['a', 'b']
>>> zip (a,b)
[(1, 'a'), (2, 'b')]
>>> zip(a,b,a)
[(1, 'a', 1), (2, 'b', 2)]
>>> zip ([1], b)
[(1, 'a')]
>>> a = ['p', 'q']; b = [[2, 3], [5, 6]]
>>> for i, (x, [_, y]) in enumerate(zip(a, b)): 
...    print i, x, y
...
0 p 3
1 q 6


#zip and list comprehensions   zip 和 list 的理解

>>> vec1 = [2, 4, 6]
>>> vec2 = [4, 3, -9]
>>> [(x, y) for x in vec1 for y in vec2]
[(2, 4), (2, 3), (2, -9), (4, 4), (4, 3), (4, -9), (6,
4), (6, 3), (6, -9)]
>>> [(vec1[i], vec2[i]) for i in range(len(vec1))]
[(2, 4), (4, 3), (6, -9)]
>>> sum([vec1[i]*vec2[i] for i in range(len(vec1))]
-34
>>> sum([x*y for (x,y) in zip(vec1, vec2)])
-34
>>> sum([v[0]*v[1] for v in zip(vec1, vec2)])
-34


#how to implement zip?   怎么实现zip?  

>>> def myzip(a,b):
	if a == [] or b == []:
    	return []
	return [(a[0], b[0])] + myzip(a[1:], b[1:])  ##一个思考  参数多了怎么实现呀

>>> myzip([1,2], ['a','b'])
[(1, 'a'), (2, 'b')]
>>> myzip([1,2], ['b'])
[(1, 'b')]