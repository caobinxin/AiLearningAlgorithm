# encoding: utf-8
import numpy as np 
a = np.array([[1.0, 2.0], [3.0, 4.0]]) 
b = np.array([[5.0, 6.0], [7.0, 8.0]]) 
sum = a + b 
difference = a - b 
product = a * b #乘法运算符执行逐元素乘法而不是矩阵乘法
quotient = a / b 
print("Sum = \n", sum)
print("Difference = \n", difference)
print("Product = \n", product)
print("Quotient = \n", quotient)


#执行矩阵乘法
matrix_product = a.dot(b) 
print("Matrix Product = ", matrix_product)


# 1D Array
a = np.array([0, 1, 2, 3, 4])
b = np.array((0, 1, 2, 3, 4))
c = np.arange(5)
d = np.linspace(0, 2*np.pi, 5)

print(a) # >>>[0 1 2 3 4]
print(b) # >>>[0 1 2 3 4]
print(c) # >>>[0 1 2 3 4]
print(d) # >>>[ 0.          1.57079633  3.14159265  4.71238898  6.28318531]
print(a[3]) # >>>3

# Basic Operators
a = np.arange(25)
a = a.reshape((5, 5))

b = np.array([10, 62, 1, 14, 2, 56, 79, 2, 1, 45,
              4, 92, 5, 55, 63, 43, 35, 6, 53, 24,
              56, 3, 56, 44, 78])
b = b.reshape((5,5))

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a ** 2)
print(a < b) 
print(a > b)

print(a.dot(b))
#除了 dot() 之外，这些操作符都是对数组进行逐元素运算。
#dot() 函数计算两个数组的点积。它返回的是一个标量（只有大小没有方向的一个值）而不是数组。

# dot, sum, min, max, cumsum
a = np.arange(10)
print(a) # >>>[0 1 2 3 4 5 6 7 8 9]    
print(a.sum()) # >>>45 所有元素的和
print(a.min()) # >>>0
print(a.max()) # >>>9
print(a.cumsum()) # >>>[ 0  1  3  6 10 15 21 28 36 45]

#cumsum()函数就不那么明显了。它将像sum()这样的每个元素相加，但是它首先将第一个元素和第二个元素相加，并将计算结果存储在一个列表中，然后将该结果添加到第三个元素中，然后再将该结果存储在一个列表中。这将对数组中的所有元素执行此操作，并返回作为列表的数组之和的运行总数。

