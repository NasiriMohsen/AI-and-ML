import tensorflow as tf

tensor1 = tf.constant([[1,1],[1,1]])
tensor2 = tf.constant([[2,2],[2,2]])

tensor = tf.matmul(tensor1,tensor2,1) #matrix multiplication same as (tensor1 @ tensor2)

print("----------------------------------------------------------------------")
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")