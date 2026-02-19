import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import n as np
import matplotlib.pyplot as plt

# Define the generator
def build_generator():
    model = keras.Sequential([
        layers.Dense(128, activation="relu", input_shape=(100,)),
        layers.BatchNormalization(),
        layers.Dense(256, activation="relu"),
        layers.BatchNormalization(),
        layers.Dense(512, activation="relu"),
        layers.BatchNormalization(),
        layers.Dense(28 * 28, activation="tanh"),
        layers.Reshape((28, 28, 1))
    ])
    return model

# Define the discriminator
def build_discriminator():
    model = keras.Sequential([
        layers.Flatten(input_shape=(28, 28, 1)),
        layers.Dense(512, activation="relu"),
        layers.Dense(256, activation="relu"),
        layers.Dense(1, activation="sigmoid")
    ])
    return model

# Compile the discriminator
discriminator = build_discriminator()
discriminator.compile(loss="binary_crossentropy", optimizer=keras.optimizers.Adam(0.0002, 0.5), metrics=["accuracy"])

generator = build_generator()

discriminator.trainable = False

# Define the GAN
z = keras.Input(shape=(100,))
img = generator(z)
validity = discriminator(img)
gan = keras.Model(z, validity)
gan.compile(loss="binary_crossentropy", optimizer=keras.optimizers.Adam(0.0002, 0.5))

# Load and preprocess the dataset
(x_train, _), (_, _) = keras.datasets.mnist.load_data()
x_train = (x_train / 127.5) - 1.0  # Normalize to [-1, 1]
x_train = np.expand_dims(x_train, axis=-1)

batch_size = 128
epochs = 10000
half_batch = batch_size // 2

for epoch in range(epochs):
    
    # Train discriminator
    idx = np.random.randint(0, x_train.shape[0], half_batch)
    real_imgs = x_train[idx]
    
    noise = np.random.normal(0, 1, (half_batch, 100))
    fake_imgs = generator.predict(noise)
    
    real_y = np.ones((half_batch, 1))
    fake_y = np.zeros((half_batch, 1))
    
    d_loss_real = discriminator.train_on_batch(real_imgs, real_y)
    d_loss_fake = discriminator.train_on_batch(fake_imgs, fake_y)
    d_loss = 0.5 * np.add(d_loss_real, d_loss_fake)
    
    # Train generator
    noise = np.random.normal(0, 1, (batch_size, 100))
    valid_y = np.ones((batch_size, 1))
    g_loss = gan.train_on_batch(noise, valid_y)
    
    # Print progress
    if epoch % 1000 == 0:
        print(f"Epoch {epoch}, D Loss: {d_loss[0]}, G Loss: {g_loss}")
        noise = np.random.normal(0, 1, (1, 100))
        generated_img = generator.predict(noise)[0]
        plt.imshow(generated_img.reshape(28, 28), cmap='gray')
        plt.show()
