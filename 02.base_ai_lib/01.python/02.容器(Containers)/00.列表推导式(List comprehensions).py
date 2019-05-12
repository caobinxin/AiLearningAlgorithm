#encoding: utf-8
#列表推导式(List comprehensions): 编程时，我们经常想要将一种数据转换为另一种数据。 举个简单的例子，思考以下计算平方数的代码：
nums = [0, 1, 2, 3, 4]
squares = []
for x in nums:
    squares.append(x ** 2)
print(squares)   # Prints [0, 1, 4, 9, 16]

#你可以使用 列表推导式 使这段代码更简单:
nums = [0, 1, 2, 3, 4]
squares = [x ** 2 for x in nums]
print(squares)   # Prints [0, 1, 4, 9, 16]

#列表推导还可以包含条件：
nums = [0, 1, 2, 3, 4]
even_squares = [x ** 2 for x in nums if x % 2 == 0]
print(even_squares)  # Prints "[0, 4, 16]"