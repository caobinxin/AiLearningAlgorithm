导入数据集有问题：
url:https://www.cnblogs.com/whiterock/p/7643363.html
错误描述：
mnist = input_data.read_data_sets("02.tensorflow/01.MNIST机器学习入门 /MNIST_data/", one_hot=True)
NameError: name 'input_data' is not defined

解决方案：
import tensorflow.examples.tutorials.mnist.input_data ==> import tensorflow.examples.tutorials.mnist.input_data as input_data
