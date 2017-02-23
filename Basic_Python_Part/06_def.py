#Defining a Function def  定义一个函数  def

不需要定义函数类型
def fact(n):
	if n == 0:
		return 1
	else:
		return fact(n) + fact(n-1)

>>>fact(5)
120

##Fibonacci Revisited   斐波那契 循环迭代
>>> a, b = 0, 1 
>>> while b <= 5:
... 	print b
...     a, b = b, a+b  #可以这样赋值
...   
1
1
2
3
5

def fib(n):
	if n <= 1:
		return n
	else:
		return fib(n-1) + fib(n-2)

>>> fib(5)
5
>>> fib(6)
8

#Default Values 函数默认值

>>> def add(a, L=[]): 
... return L + [a]   //"+" 和 append 不同 a=[1],L=[2]  L+a=[1,2] if L.append(a) L=[2,[1]]
... >>> add(1)
	[1]
>>> add(1,1)
	error!
>>> add(add(1))
	[[1]]
>>> add(add(1), add(1))
[1, [1]]