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

# Creating the model
model = tf.keras.models.Sequential([
    # Flatten the 3D input to a 1D vector
    tf.keras.layers.Flatten(input_shape=(img_height, img_width, 3)),
    # Add the neuron layers
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(10, activation='relu'),
    tf.keras.layers.Dense(2, activation='sigmoid')
])

print(model.summary())

# Compiling the model with the requested parameters
model.compile(optimizer='SGD',
              loss='categorical_crossentropy',
              metrics='accuracy')

model.fit(
    train_data,
    epochs=10)

print()
print("Validation data")
validation_loss, validation_acc = model.evaluate(validation_data)
print("Validation loss:", validation_loss)
print("Validation accuracy:", validation_acc)
