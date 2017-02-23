#Sets  集合

##identity maps, unordered collection  映射 无序
##[] for lists, () for tuples, {} for dicts, and {} for sets (2.7)

# in, not in, add, remove

>>> a = {1, 2}
a
>> set([1, 2])
>>> a = set((1,2)) 
>>> a
set([1, 2])
>>> b = set([1,2])
>>> a == b
True
>>> c = set({1:'a', 2:'b'}) 
>>> c
set([1, 2])

>>> a = set([]) 
>>> 1 in a False
>>> a.add(1) 
>>> a.add('b') 
>>> a
set([1, 'b']) 
>>> a.remove(1) 
>>> a set(['b'])

#Set Operations 集合运算  
##union, intersection, difference, is_subset, etc.. 并 交  非子集部分  子集 等

>>> a = set('abracadabra')
>>> b = set('alacazam')
>>> a
set(['a', 'r', 'b', 'c', 'd']) 
>>> a - b
set(['r', 'd', 'b'])
>>> a | b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l']) 
>>> a & b
set(['a', 'c'])
>>> a ^ b
set(['r', 'd', 'b', 'm', 'z', 'l'])
>>> a |= b
>>> a
set(['a', 'c', 'b', 'd', 'm', 'l', 'r', 'z'])

#Set type

len(s)
x in s
x not in s
s.is_subset(t)     					#s <= t
s.issuperset(t)	   					#s >= t
s.union(t)
s.intersection(t)  					#s & t
s.defference(t) 
s.symmetric_difference(t) 			#s ^ t    ！(s & t)
s.copy()
s.update(t)							#s != t
s.intersection_update(t)			#s &= t
s.difference_update(t)				#s -= t
s.symmetric_difference_update(t)	#s ^= t
s.add(x)
s.remove(x)
s.discard(x)						#s中存在x则删除
s.pop()
s.clear()