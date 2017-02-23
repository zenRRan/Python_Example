#break, continue and else

#break and continue 和C/Java的一样
# else就有那么点区别：
# 	1：就是if 后的else
# 	2：在循环中断的后面，比如 求素数：
		 >>> for n in range(2, 10):
		... 	for x in range(2, n):
    	...			if n % x == 0:
		...				break
		... 	else:
					print n,    #逗号是为了输出后不换行