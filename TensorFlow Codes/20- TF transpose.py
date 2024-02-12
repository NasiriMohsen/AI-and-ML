import tensorflow as tf

tensor1 = tf.constant([[1,2,3],[4,5,6],[7,8,9]])

tensor2 = tf.transpose(tensor1)

print("----------------------------------------------------------------------")
print("tensor1: ")
print(tensor1)
print(type(tensor1))
print("")
print("tensor2: ")
print(tensor2)
print(type(tensor2))
print("----------------------------------------------------------------------")