#数值计算e的x次幂, x在-1和1之间；（泰勒展开）


def Taylor(x):
    maxRound = 1000
    num = 1.
    xx = 1.
    xPow = 1.
    mini = 1.5e-40
    for i in range(maxRound):
       if i == 0:
            continue
       else:
            xx *= i
            xPow *= x
            y = 1 / xx * xPow
            if(y < mini):
                return num
            num += y

readInt = input("input a number around -1 to 1\n")
n = float(readInt)
if n < -1 or n > 1:
    print("input error")
else:
    print(Taylor(n))

