import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import tensorflow as tf

#hello_constant = tf.constant('Hello World!')
#with tf.Session() as sess:
#    output = sess.run(hello_constant)
#    print(output)

# this is how you create an input field in Tensorflow
# not the tf.string part but the tf.placeholder part 
# the tf.string part is just the type of placeholder that this specific case is

x = tf.placeholder(tf.string)
y = tf.placeholder(tf.int32)
z = tf.placeholder(tf.float32)


with tf.Session() as sess:
    #output = sess.run(x, feed_dict={x: 'Hello World' })
    output = sess.run([x, y, z], feed_dict={x: 'Test String', y:123, z: 45.67}) 
    print(output)
    


