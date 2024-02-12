import tensorflow as tf

tensor1 = tf.constant([1, 2, 3, 4, 5])

tensor2 = tf.reduce_sum(tensor1,0)

print("----------------------------------------------------------------------")
print(tensor2)
print(type(tensor2))
print("----------------------------------------------------------------------")