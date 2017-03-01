#给定一段文本，按照频率降序排列每个文本里面出现的词，并且打印出词频。

file_path = "data.txt"
file = open(file_path)
sent = []
for line in file.readlines():
    refresh = line.split(" ")
    while "" in refresh:
        refresh.remove("")
    sent.extend(refresh)
# print(sent)
l = list(set(sent))
# print(l)
value = []
for word in l:
    value.extend(str(sent.count(word)))
for i in range(len(value)):
    value[i] = int(value[i])
dic = dict(zip(l, value))
print(dic)
print(sorted(dic.items(), key=lambda d: d[1])[::-1])


