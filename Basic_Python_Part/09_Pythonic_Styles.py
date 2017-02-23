#Pythonic Styles 

#do not write ...           when you can write ...
for key in d.keys():		for key in d:

if d.has_key(key):			if key in d:

i=0 						for i, x in enumerate(a):
for x in a:				
...
i += 1

a[0:len(a) - i]				a[:-i]

for line in \
    sys.stdin.readlines():	for line in sys.stdin:

for x in a:					print " ".join(map(str, a))  # 把a的元素映射成str类型，再拼接
    print x,
print

s = ""						print " " * lev
for i in range(lev):
s += " " 
print s