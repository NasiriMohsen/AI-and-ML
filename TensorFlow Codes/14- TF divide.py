import tensorflow as tf

tensor1 = tf.constant([2, 6, 12, 20, 30])
tensor2 = tf.constant([1, 2, 3, 4, 5])

tensor = tf.divide(tensor1,tensor2) 

print("----------------------------------------------------------------------")
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")