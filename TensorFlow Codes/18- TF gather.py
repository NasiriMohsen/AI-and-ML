import tensorflow as tf

tensor1 = tf.constant([1,2,3,4,5,6,7,8,9])
tensor2 = tf.constant([0,3,5,7])

tensor = tf.gather(tensor1,tensor2) #shows the sepcified houses

print("----------------------------------------------------------------------")
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")