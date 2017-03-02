file_path = "data.txt"
# file_path = "data.txt"
file = open(file_path)
sent = []
for line in file.readlines():
    # print(line,end="")
    refresh = line.strip().split(" ")
    while "" in refresh:
        refresh.remove("")
    while '\\n' in refresh:
        refresh.remove('\n')
    while '\t' in refresh:
        refresh.remove('\t')
    sent.extend(refresh)

l = list(set(sent))
# print(l)
value = []
for word in l:
    # value.extend(str(sent.count(word)))
    value.append(sent.count(word))
    # print(word,sent.count(word))
for i in range(len(value)):
    value[i] = int(value[i])
dic = dict(zip(l, value))
# print(dic)
print(sorted(dic.items(), key=lambda d: d[1])[::-1])
# print(len(dic))


