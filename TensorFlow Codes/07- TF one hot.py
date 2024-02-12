import tensorflow as tf

Labels = [1,2,1,1,0,0] 
depthValue = max(Labels) + 1
tensor = tf.one_hot(Labels,depthValue)

print("----------------------------------------------------------------------")
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")