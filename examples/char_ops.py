#给定一个字符串，判断该字符串是否满足：{对于字符串中任意两个字符c1, c2， count(c1) == count(c2)}；
import numpy as np

def one(sent):
    s = set(sent)
    l = list(s)
    maxCount = sent.count(l[0])
    for x in l:
        if maxCount != sent.count(x):
            return False
    return True

sent = input("input a string\n")
if(len(sent) == 0):
    print("no input snetence")
elif(len(sent) == 1):
    print("True")
else:
    print(one(sent))

###########################################################################################




