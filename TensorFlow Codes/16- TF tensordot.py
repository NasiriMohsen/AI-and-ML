import tensorflow as tf

tensor1 = tf.constant([2, 4, 6, 8])
tensor2 = tf.constant([1, 2, 3, 4])

tensor = tf.tensordot(tensor1,tensor2,1) #sum(tensor1 * tensor2) 2 + 8 + 18 + 32

print("----------------------------------------------------------------------")
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")