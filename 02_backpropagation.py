import tensorflow as tf

# 反向传播

w = tf.Variable(tf.constant(5, dtype=tf.float32))
lr = 0.2
epoch = 40

# 测试gpu是否可用
# print(tf.test.is_gpu_available())

for epoch in range(epoch):
    with tf.GradientTape() as tape:
        loss = tf.square(w + 1)
    grads = tape.gradient(loss, w)

    w.assign_sub(lr * grads)
    print("After %s epoch, wis %f ,loss is %f" % (epoch, w.numpy(), loss))
