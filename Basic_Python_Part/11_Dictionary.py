#Dictionaries 字典   

##hash maps

#Constructing Dicts  构造字典
##key : value pairs  键: 值

>>> d = {'a': 1, 'b': 2, 'c': 1}
>>> d['b']
2
>>> d['b'] = 3
>>> d['b']
3
>>> d['e']
KeyError!
>>> d.has_key('a')
True
>>> 'a' in d
True
>>> d.keys()
['a', 'c', 'b']
>>> d.values()
[1, 1, 3]

#Other Constructions 其他构造方法

>>> d = {'a': 1, 'b': 2, 'c': 1}
>>> keys = ['b', 'c', 'a'] 
>>>values=[2,1, 1]
>>> e = dict (zip (keys, values)) 
>>> d == e
True
>>> d.items()
[('a', 1), ('c', 1), ('b', 2)]
>>> f = dict( [(x, x**2) for x in values] )
>>> f
{1: 1, 2: 4}
>>> g = dict(a=1, b=2, c=1)
>>> g == d
True

#default values  默认值

##counting frequencies 计数频率

>>> def incr(d, key):
... 	if key not in d:
... 		d[key] = 1
... 	else:
...			d[key] += 1
...

>>> def incr(d, key):
...      d[key] = d.get(key, 0) + 1
...
>>> incr(d, 'z')
>>> d
{'a': 1, 'c': 1, 'b': 2, 'z': 1}
>>> incr(d, 'b')
>>> d
{'a': 1, 'c': 1, 'b': 3, 'z': 1}

#defaultdict类  best feature introduced in Python 2.5

>>> from collections import defaultdict
>>> d = defaultdict(int)
>>> d['a']
0
>>> d['b'] += 1
>>> d
{'a': 0, 'b': 1}
>>> d = defaultdict(list)
>>> d['b'] += [1]
>>> d
{'b': [1]}
>>> d = defaultdict(lambda : <expr>)

#Mapping Type
##字面有的很容易理解

len(a)					
a[k]
a[k] = v  				
del a[k]
a.clear()
a.copy()
a.has_key(k)
k in a
k not in a
a.items()
a.values()
a.get(k[, x])				#a[k] if k in a, else x
a.setdefault(k[, x]) 		#a[k] if k in a, else x (also setting it 可以说是重新设置数据)
a.pop(k[, x])				#a[k] if k in a, else x (also remove k 也可以说是删除k)