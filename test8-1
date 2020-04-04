import tensorflow as tf

x=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])

a_x=tf.reduce_mean(x)
a_y=tf.reduce_mean(y)
x1=tf.subtract(x,a_x)
y1=tf.subtract(y,a_y)
w1=tf.reduce_sum(tf.multiply(x1,y1))
w2=tf.square(x1)
w3=tf.reduce_sum(w2)
w=tf.divide(w1,w3)
print("w=")
print(w.numpy())

a_w=tf.multiply(w,a_x)
b=tf.subtract(a_y,a_w)
print("b=")
print(w.numpy())
