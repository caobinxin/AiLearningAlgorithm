# encoding: utf-8
import numpy as np 

my_2d_array = np.zeros((2, 3)) 
print (my_2d_array)

my_2d_array_new = np.ones((2, 4)) 
print (my_2d_array_new)

#像上面那样的多维数组可以用 my_array[i][j] 符号来索引，其中i表示行号，j表示列号。i和j都从0开始
my_array = np.array([[4, 5], [6, 1]])
print(my_array[0][1])
print (my_array.shape)

my_array_column_2 = my_array[:, 1] 
print (my_array_column_2)

