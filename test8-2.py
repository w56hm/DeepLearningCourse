import tensorflow as tf
x=tf.constant([64.3,99.6,145.45,63.75,135.46,92.85,86.97,144.76,59.3,116.03])
y=tf.constant([62.55,82.42,132.62,73.31,131.05,86.57,85.49,127.44,55.25,104.84])
z=tf.multiply(x,y)
z1_sum=tf.reduce_sum(z)
x_sum=tf.reduce_sum(x)
y_sum=tf.reduce_sum(y)
z2_sum=tf.multiply(x_sum,y_sum)
s1=tf.subtract(z1_sum,z2_sum)
x1_sum=tf.reduce_sum(tf.square(x))*(x.numpy().size)
x2_sum=tf.square(x_sum)
s2=tf.subtract(x1_sum,x2_sum)
w=tf.divide(s1,s2)
print("w=")
print(w.numpy())

wxi=tf.multiply(w,x_sum)
s3=tf.subtract(y_sum,wxi)
n=x.numpy().size
b=tf.divide(s3,n)
print("b=")
print(b.numpy())
