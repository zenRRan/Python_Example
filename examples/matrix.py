#矩阵乘法运算，给定矩阵A，计算A的3次方，A的逆矩阵，A的行列式值，A的特征值；（可以使用相关库）

import numpy as np

def Matrix_ops(mat):
    print(mat,"\n的三次方：\n", mat**3)
    print("逆矩阵：\n", np.linalg.inv(mat))
    print("行列式值：\n", np.linalg.det(mat))
    a, _ = np.linalg.eig(mat) #a是特征值，_是特征向量
    print("特征值：\n", a)

mat = np.array([[1,2],
                [3,4]])
Matrix_ops(mat)