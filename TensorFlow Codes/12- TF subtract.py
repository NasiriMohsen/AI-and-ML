import tensorflow as tf

tensor1 = tf.constant([3, 4, 5, 6, 7])
tensor2 = tf.constant([1, 2, 3, 4, 5])

tensor = tf.subtract(tensor1,tensor2) 

print("----------------------------------------------------------------------")
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")