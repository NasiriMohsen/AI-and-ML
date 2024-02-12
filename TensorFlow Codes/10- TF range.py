import tensorflow as tf

#tensor = tf.range(10)
#tensor = tf.range(start=0,limit=10,delta=1)

#tensor = tf.range(start=1,limit=10,delta=2) #Odd Numbers
#tensor = tf.range(start=2,limit=10,delta=2) #Even Numbers

tensor = tf.range(start=0,limit=10,delta=3)

print("----------------------------------------------------------------------")
print(tensor)
print(type(tensor))
print("----------------------------------------------------------------------")