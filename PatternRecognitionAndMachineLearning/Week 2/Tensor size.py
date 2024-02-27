'''
DATA.ML.100 # Purpose of code
Creator: Valtteri Nikkanen
Student number: 282688
'''

import tensorflow as tf

# declare input shape
input = tf.keras.Input(shape=(100,100,1))

# Block 1 (convolution)
conv1 = tf.keras.layers.Conv2D(64, 1, strides=1, activation="relu")(input)
#x = tf.keras.layers.MaxPooling2D(3)(x)
#x = tf.keras.layers.BatchNormalization()(x)
print(conv1.shape)
# Block 2 (convolution 2)
conv2 = tf.keras.layers.Conv2D(128, 1, strides=1, activation="relu")(
    conv1)
#x = tf.keras.layers.BatchNormalization()(x)
#x = tf.keras.layers.Dropout(0.3)(x)

# Now that we apply global max pooling.
#gap = tf.keras.layers.GlobalMaxPooling2D()(x)
"""
# Block 3 (full connected9)
fc = tf.keras.layers.Flatten()(conv2)
fc = tf.keras.layers.Dense(10)(fc)


# Finally, we add a classification layer.
output = tf.keras.layers.Dense(10, activation="softmax")(fc)

# bind all
cnn_model = tf.keras.Model(input, output)
"""
print(conv2.shape)