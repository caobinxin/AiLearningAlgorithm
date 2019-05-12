# encoding: utf-8
import numpy as np 
# Boolean masking
import matplotlib.pyplot as plt

a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a,b)
mask = b >= 0
# print(mask)
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()

#上面的示例显示了如何进行布尔屏蔽。你所要做的就是将数组传递给涉及数组的条件，它将为你提供一个值的数组，为该条件返回true。

#我们利用这些条件来选择图上的不同点。蓝色点(在图中还包括绿点，但绿点掩盖了蓝色点)，显示值大于0的所有点。绿色点表示值大于0且小于一半π的所有点。
