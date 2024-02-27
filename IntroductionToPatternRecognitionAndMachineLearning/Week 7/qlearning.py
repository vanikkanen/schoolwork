import gym
import numpy as np
import matplotlib.pyplot as plt


def eval_policy(qtable_, num_of_episodes_, max_steps_):
    rewards = []

    for episode in range(num_of_episodes_):
        state = env.reset()
        state = state[0]
        step = 0
        done = False
        total_rewards = 0

        for step in range(max_steps_):
            action = np.argmax(qtable_[state])
            new_state, reward, truncated, done, info = env.step(action)
            total_rewards += reward

            if done:
                rewards.append(total_rewards)
                break
            state = new_state

    env.close()
    avg_reward = sum(rewards)/num_of_episodes_
    return avg_reward


env = gym.make("FrozenLake-v1", is_slippery=True, render_mode="ansi")
env.reset()
print(env.render())

state, reward, done, truncated, info = env.step(1)
print(env.render())

states = env.observation_space.n
actions = env.action_space.n

episodes = 250
max_steps = 150
# Discount factor
gamma = 0.9
# Learning rate
alpha = 0.5

for run in range(10):
    reward_hist = []
    episode_hist = []
    Q = np.zeros([states, actions])

    print(run)

    for episode in range(episodes+1):
        state = env.reset()
        state = state[0]
        step = 0
        done = False

        for step in range(max_steps):
            random_action = env.action_space.sample()
            new_state, reward, done, truncated, info = env.step(random_action)
            if state != new_state:
                # Deterministic update rule
                Q[state][random_action] = reward + gamma*(np.amax(Q[
                 new_state]))
                # Non-deterministic update rule
                #Q[state][random_action] += alpha*(reward + gamma*(np.amax(Q[
                #new_state]))-Q[state][random_action])
            state = new_state
            if done:
                break

        if episode % 10 == 0:
            reward_hist.append(eval_policy(Q, 100, 100))
            episode_hist.append(episode)
    plt.plot(episode_hist, reward_hist, label=run)


env.reset()
plt.ylabel('Average reward')
plt.xlabel('Episode')
plt.show()