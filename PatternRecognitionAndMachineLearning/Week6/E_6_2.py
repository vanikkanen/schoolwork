import gym
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def evaluate(model, env, episodes=10, interactions=100):
    rewards = []
    for episode in range(episodes):
        state = env.reset()[0]
        done = False
        total_reward = 0
        step = 0
        while not done:

            one_hot_state = tf.one_hot(state, depth=state_size)
            q_values = model.predict(one_hot_state.numpy().reshape(1, -1))
            action = np.argmax(q_values)
            state, reward, done, truncated, info = env.step(action)
            total_reward += reward
            if step > interactions:
                done = True
            step += 1
        rewards.append(total_reward)
    return np.mean(rewards)


def run_animation(experience_buffer):
    time_lag = 500  # Delay (in s) between frames
    fig = plt.figure()

    ims = []
    for experience in experience_buffer:
        im = plt.imshow(experience["frame"], animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims,
                                    interval=time_lag, blit=True, repeat=False)
    plt.show()


env = gym.make("Taxi-v3", render_mode="rgb_array")
action_size = env.action_space.n
print("Action size: ", action_size)
state_size = env.observation_space.n
print("State size: ", state_size)

model = tf.keras.models.Sequential([
  tf.keras.layers.InputLayer(input_shape=(state_size,)),
  tf.keras.layers.Dense(32, activation='relu'),
  tf.keras.layers.Dense(32, activation='relu'),
  tf.keras.layers.Dense(action_size, activation='linear')
])
loss_fn = tf.keras.losses.MeanSquaredError()
opt = tf.keras.optimizers.Adam()
model.compile(optimizer=opt,
              loss=loss_fn,
              metrics=['mse'])

model.summary()

with open("qtable.npy", "rb") as f:
    qtable = np.load(f)

print(f"Qtable shape: {qtable.shape}")

one_hot_states = np.identity(state_size)

# train the model
model.fit(one_hot_states, qtable, epochs=200, verbose=1)

interactions = 100

val_mean = evaluate(model, env)

print(f"Mean value for the NN: {val_mean}")

state = env.reset()[0]
step = 0
done = False
total_rewards = 0
experience_buffer = []
while not done:
    one_hot_state = tf.one_hot(state, depth=state_size)
    q_values = model.predict(one_hot_state.numpy().reshape(1, -1))
    action = np.argmax(q_values)
    state, reward, done, truncated, info = env.step(action)
    experience_buffer.append({
                    'frame': env.render(),
                    'state': state,
                    'action': action,
                    'reward': total_rewards})

print("Animation")
run_animation(experience_buffer)

env.close()

