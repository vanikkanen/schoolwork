from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
import tensorflow as tf

print(tf.__version__)

# to disable GPU
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'

if tf.test.gpu_device_name():
    print('GPU found')
else:
    print("No GPU found")

batch_size = 32
img_height = 64
img_width = 64

# Some parameters that do data augmentation for us
train_datagen = ImageDataGenerator(
    rescale=1./255,
    validation_split=0.2,
    rotation_range=10,
    width_shift_range=0.1,
    height_shift_range=0.1,
    zoom_range=0.1
)

train_data = train_datagen.flow_from_directory(
    'GTSRB_subset_2',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    seed=123  # Using seed to get the same images with different runs
)

validation_data = train_datagen.flow_from_directory(
    'GTSRB_subset_2',
    target_size=(img_height, img_width),
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation',
    seed=123  # Using seed to get the same images with different runs
)

# declare input shape
input = tf.keras.Input(shape=(64, 64, 3))

# Block 1 (convolution + max pooling)
conv1 = tf.keras.layers.Conv2D(10, (3, 3), strides=2, activation="relu")(input)
max1 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv1)

# Block 2 (convolution2 + max pooling2)
conv2 = tf.keras.layers.Conv2D(10, (3, 3), strides=2, activation="relu")(max1)
max2 = tf.keras.layers.MaxPooling2D(pool_size=(2, 2))(conv2)

# Flattening
fc = tf.keras.layers.Flatten()(max2)

# Finally, we add a classification layer.
output = tf.keras.layers.Dense(2, activation="sigmoid")(fc)

# bind all
cnn_model = tf.keras.Model(input, output)

# This loss takes care of one-hot encoding
loss_fn = tf.keras.losses.BinaryCrossentropy(from_logits=True)

cnn_model.compile(loss=loss_fn, optimizer="SGD", metrics=["accuracy"])
cnn_model.summary()

history = cnn_model.fit(train_data, batch_size=32, epochs=20)

validation_loss, validation_acc = cnn_model.evaluate(validation_data)
print("Validation loss:", validation_loss)
print("Validation accuracy:", validation_acc)
