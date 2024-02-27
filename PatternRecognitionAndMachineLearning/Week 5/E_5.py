import random
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import tensorflow as tf
import numpy as np
from tensorflow.keras.models import Model
import matplotlib.pyplot as plt

print(tf.config.list_physical_devices('GPU'))

fashion_mnist = tf.keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0

test_images = test_images / 255.0

print (train_images.shape)
print (test_images.shape)

noise_factor = 0.2
train_images_noisy = train_images + noise_factor * tf.random.normal(shape=train_images.shape)
test_images_noisy = test_images + noise_factor * tf.random.normal(shape=test_images.shape)
# Make sure values still in (0,1)
train_images_noisy = tf.clip_by_value(train_images_noisy,clip_value_min=0., clip_value_max=1.)
test_images_noisy = tf.clip_by_value(test_images_noisy,clip_value_min=0., clip_value_max=1.)

# Defining a CNN model

# declare input shape
input = tf.keras.Input(shape=(28,28,1))
# Block 1 (convolution)
conv1 = tf.keras.layers.Conv2D(32, 3, strides=1, activation="relu")(input)
#x = tf.keras.layers.MaxPooling2D(3)(x)
#x = tf.keras.layers.BatchNormalization()(x)
# Block 2 (convolution 2)
conv2 = tf.keras.layers.Conv2D(64, 3, strides=1, activation="relu")(conv1)
# Block 3 (full connected9)
fc = tf.keras.layers.Flatten()(conv2)
fc = tf.keras.layers.Dense(10)(fc)
# Finally, we add a classification layer.
output = tf.keras.layers.Dense(10, activation="softmax")(fc)
# bind all
cnn_model = tf.keras.Model(input, output)
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)
cnn_model.compile(loss=loss_fn, optimizer="adam", metrics=["accuracy"])
cnn_model.summary()

history = cnn_model.fit(train_images, train_labels, epochs=10)

test_loss, test_acc = cnn_model.evaluate(test_images,  test_labels, verbose=2)
print('\nTest accuracy for clean images:', test_acc)

test_loss, test_acc = cnn_model.evaluate(test_images_noisy,  test_labels,
                                         verbose=2)
print('\nTest accuracy for noisy images:', test_acc)

train_images = train_images[..., tf.newaxis]
test_images = test_images[..., tf.newaxis]
train_images_noisy = train_images_noisy[..., tf.newaxis]
test_images_noisy = test_images_noisy[..., tf.newaxis]


class Denoise(Model):

    def __init__(self):
        super(Denoise, self).__init__()
        self.encoder = tf.keras.Sequential([
          tf.keras.layers.Input(shape=(28, 28, 1)),
          tf.keras.layers.Conv2D(16, (3, 3), activation='relu', padding='same', strides=2),
          tf.keras.layers.Conv2D(8, (3, 3), activation='relu', padding='same', strides=2)])

        self.decoder = tf.keras.Sequential([
          tf.keras.layers.Conv2DTranspose(8, kernel_size=3, strides=2, activation='relu', padding='same'),
          tf.keras.layers.Conv2DTranspose(16, kernel_size=3, strides=2, activation='relu', padding='same'),
          tf.keras.layers.Conv2D(1, kernel_size=(3, 3), activation='sigmoid', padding='same')])

    def call(self, x):
        encoded = self.encoder(x)
        decoded = self.decoder(encoded)
        return decoded

autoencoder = Denoise()

autoencoder.compile(optimizer='adam', loss=tf.keras.losses.MeanSquaredError())

autoencoder.fit(train_images_noisy, train_images,
                epochs=10,
                shuffle=True,
                validation_data=(test_images_noisy, test_images))

encoded_imgs = autoencoder.encoder(test_images).numpy()
decoded_imgs = autoencoder.decoder(encoded_imgs).numpy()

n = 10
plt.figure(figsize=(20, 4))
for i in range(n):

    img_ind = random.randrange(len(test_images))

    # display original + noise
    ax = plt.subplot(2, n, i + 1)
    plt.title("original + noise")
    plt.imshow(tf.squeeze(test_images_noisy[img_ind]))
    plt.gray()
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    # display reconstruction
    bx = plt.subplot(2, n, i + n + 1)
    plt.title("reconstructed")
    plt.imshow(tf.squeeze(decoded_imgs[img_ind]))
    plt.gray()
    bx.get_xaxis().set_visible(False)
    bx.get_yaxis().set_visible(False)
plt.show()

denoised_test_images = autoencoder.call(test_images_noisy)

test_loss, test_acc = cnn_model.evaluate(denoised_test_images,  test_labels,
                                         verbose=2)
print('\nTest accuracy for denoised images:', test_acc)

#tf.keras.backend.clear_session()
history = cnn_model.fit(train_images_noisy, train_labels, epochs=10)

test_loss, test_acc = cnn_model.evaluate(test_images_noisy,  test_labels,
                                         verbose=2)
print('\nTest accuracy with noisy trained model for noisy images:', test_acc)
