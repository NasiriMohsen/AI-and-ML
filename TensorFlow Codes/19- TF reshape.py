import tensorflow as tf

tensor1 = tf.constant([0,1,2,3,4,5,6,7,8,9])

tensor2 = tf.reshape(tensor1,(5,2))

print("----------------------------------------------------------------------")
print(tensor2)
print(type(tensor2))
print("----------------------------------------------------------------------")