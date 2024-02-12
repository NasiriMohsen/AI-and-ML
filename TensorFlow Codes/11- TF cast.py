import tensorflow as tf

tensor1 = tf.constant([1,1,1,0,0])

tensor2 = tf.cast(tensor1,tf.int16) #tf.int 8,16,32,64 or tf.float 16,32,64 or tf.bool

print("----------------------------------------------------------------------")
print("tensor1: ")
print(tensor1)
print(type(tensor1))
print("")
print("tensor2: ")
print(tensor2)
print(type(tensor2))
print("----------------------------------------------------------------------")