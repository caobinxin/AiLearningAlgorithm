# encoding: utf-8
import numpy as np 
my_array = np.array([1, 2, 3, 4, 5]) 
print (my_array)

print (my_array.shape) #它会打印我们创建的数组的形状：(5, )。意思就是 my_array 是一个包含5个元素的数组。

print (my_array[0])
print (my_array[1])

my_array[0] = -1
print (my_array)

my_new_array = np.zeros((5)) #创建一个长度为5的NumPy数组，但所有元素都为0，
print (my_new_array)

my_new_array = np.ones((5)) #创建一个长度为5的NumPy数组，但所有元素都为1，
print (my_new_array)


my_random_array = np.random.random((5))#随机值 它为每个元素分配0到1之间的随机值。
print (my_random_array)