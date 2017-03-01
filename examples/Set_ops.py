#给定两个集合，每个集合里面包含若干开区间或者闭区间，求这两个集合的交集，并集，以及里面的所包含的具体整数集合 ；

#数据规范：(10 20],[50 90]  [11 15],[16 80)  两个集合之间用2空格隔开  集合内部用小集合以英文逗号隔开,小集合中的数据以1个空格隔开 其他不能有空格，集合必须按照从小打到排列

def merge(L0, L1, L2, L3):
    str = []
    BF = ""
    S = 1.5e-45
    E = 1.5e-45
    EF = ""
    cell = []
    B = []
    first = []
    over = []
    O = []
    for (b_flag, start, end, e_flag) in zip(L0, L1, L2, L3):
        # print(start, end)
        if S == 1.5e-45:
            BF = b_flag
            S = start
            E = end
            EF = e_flag
            continue
        if E > start and E <= end:
            E = end
            EF = e_flag
            continue
        else:
            str += (BF+S+E+EF)
            # print("%s%d %d%s" %(BF,S,E,e_flag),end="")
            print(BF,S,",",E,EF," ",end="")
            B.append(BF)
            first.append(S)
            over.append(E)
            O.append(EF)
            BF = b_flag
            S = start
            E = end
            EF = e_flag
            continue
    print(BF, S, ",", E, EF, " ")
    B.append(BF)
    first.append(S)
    over.append(E)
    O.append(EF)
    return (B, first, over, O)

def Int_num(B, first, over, O):
    number = []
    for b,x,y,o in zip(B, first, over, O):
        cell = []
        f = int(x)
        e = int(y)
        for i in range(f, e+1):
            cell.append(i)
        if b == "(":
            cell.pop(0)
        if o == ")":
            cell.pop()
        # print(cell)
        number.extend(cell)
    return number

file_path = "Set_ops_data.txt"
file = open(file_path)
#处理数据
for line in file:
    line = line.strip()
    print("数据：\n",line)
    sent = line.split("  ")
    # print(sent)
    sets_1 = sent[0]
    sets_2 = sent[1]
    sets_1 = sets_1.split(",")
    sets_2 = sets_2.split(",")
    # print(sets_1,sets_2)
    data_1 = []
    data_2 = []
    for x in sets_1:
        x = x.split(" ")
        cell = []
        cell.append(x[0][0])
        cell.append(int(x[0][1:len(x[0])]))
        cell.append(int(x[1][:-1]))
        cell.append((x[1][-1]))
        data_1.append(cell)
    # print(data_1)
    for x in sets_2:
        x = x.split(" ")
        cell = []
        cell.append(x[0][0])
        cell.append(int(x[0][1:len(x[0])]))
        cell.append(int(x[1][:-1]))
        cell.append((x[1][-1]))
        data_2.append(cell)
    # print(data_2)

    #并集
    new_data = []
    L0 = []
    L1 = []
    L2 = []
    L3 = []
    for set1 in data_1:
        for set2 in data_2:
            if set1[1] > set2[2] or set1[2] < set2[1]:
                continue
            begin_flag = set1[0]
            begin_num = set1[1]
            end_flag = set1[3]
            end_num = set1[2]
            if set1[1] > set2[1]:
                begin_num = set2[1]
                begin_flag = set2[0]
            if set1[2] < set2[2]:
                end_num = set2[2]
                end_flag = set2[3]
            cell = begin_flag+str(begin_num)+" "+str(end_num)+end_flag
            L0.append(begin_flag)
            L1.append(str(begin_num))
            L2.append(str(end_num))
            L3.append(end_flag)
            new_data.append(cell)
    # print(new_data)
    # print(L1 ,L2)
    print("并集")
    B, first, over, O = merge(L0, L1, L2, L3)
    print("整数集合：",Int_num(B, first, over, O))

    #交集
    new_data = []
    L0 = []
    L1 = []
    L2 = []
    L3 = []
    for set1 in data_1:
        for set2 in data_2:
            if set1[1] > set2[2] or set1[2] < set2[1]:
                continue
            begin_flag = set1[0]
            begin_num = set1[1]
            end_flag = set1[3]
            end_num = set1[2]
            if set1[1] < set2[1]:
                begin_num = set2[1]
                begin_flag = "["
            if set1[2] > set2[2]:
                end_num = set2[2]
                end_flag = set2[3]
            cell = begin_flag+str(begin_num)+" "+str(end_num)+end_flag
            L0.append(begin_flag)
            L1.append(str(begin_num))
            L2.append(str(end_num))
            L3.append(end_flag)
            new_data.append(cell)
    # print(new_data)
    # print(L1, L2)

    print("交集")
    B, first, over, O = merge(L0, L1, L2, L3)
    print("整数集合：",Int_num(B, first, over, O))
    print()








