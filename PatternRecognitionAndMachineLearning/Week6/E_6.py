import gym
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def eval_policy_better(env_, pi_, gamma_, t_max_, episodes_):
    env_.reset()

    v_pi_rep = np.empty(episodes_)
    rewards = np.empty(episodes_)
    for e in range(episodes_):
        total_reward = 0
        s_t = env.reset()[0]
        v_pi = 0
        for t in range(t_max_):
            a_t = pi_[s_t]
            s_t, r_t, done, truncated, info = env_.step(a_t)
            v_pi += gamma_**t*r_t
            total_reward += r_t
            if done:
                break

        rewards[e] = total_reward
        v_pi_rep[e] = v_pi
    #return np.mean(v_pi_rep), np.min(v_pi_rep), np.max(v_pi_rep), np.std(
    # v_pi_rep)
    return np.mean(rewards), np.min(rewards), np.max(rewards), np.std(rewards)


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

done = False

# Q-Table driving
qtable = np.zeros((state_size, action_size))  # Taxi
episodes = 5000  # num of training episodes
interactions = 100  # max num of interactions per episode
epsilon = 0.99  # e-greedy
alpha = 0.1  # learning rate - 1.
gamma = 0.9  # reward decay rate
debug = 0
hist = []  # evaluation history

experience_buffer = []

# Main Q-learning loop
for episode in range(episodes):

    epsilon = max(0.01, 1.0 - episode / episodes)

    state = env.reset()[0]
    step = 0
    done = False
    total_rewards = 0

    for interact in range(interactions):
        # exploitation vs. exploration by e-greedy sampling of actions
        if np.random.uniform(0, 1) > epsilon:
            action = np.argmax(qtable[state, :])
        else:
            action = np.random.randint(0, 6)

        # Observe
        new_state, reward, done, truncated, info = env.step(action)
        total_rewards += reward

        # Update Q-table
        qtable[state, action] = qtable[state, action] + alpha * (reward + gamma * np.max(qtable[new_state, :]) - qtable[state, action])

        # Our new state is state
        state = new_state
        if episode == episodes-1:
            experience_buffer.append({
                'frame': env.render(),
                'episode': episode,
                'state': state,
                'action': action,
                'reward': total_rewards
            }
            )
        # Check if terminated
        if done == True:
            break

    if episode % 100 == 0 or episode == 1:
        #print(episode)
        pi = np.argmax(qtable, axis=1)
        val_mean, val_min, val_max, val_std = \
            eval_policy_better(env, pi, gamma, interactions, 1000)
        hist.append([episode, val_mean, val_min, val_max, val_std])
        if debug == True:
            print(pi)
            print(val_mean)


env.reset()

print("Animation")
run_animation(experience_buffer)

hist = np.array(hist)
print(hist.shape)

print(f"Mean reward of final qtable: {hist[len(hist)-1, 1]}")
plt.errorbar(hist[:, 0], hist[:, 1], yerr=hist[:, 4])
plt.show()
with open("qtable.npy", "wb") as f:
    np.save(f, qtable)

"""
# Manual driving
env.reset()
env.render()
score = 0
while not done:
    action = int(input('0/south 1/north 2/east 3/west 4/pickup 5/drop off:'))
    new_state, reward, done, truncated, info = env.step(action)
    score += reward
    time.sleep(1.0)
    print(f'S_t+1={new_state}, r_t+1={reward}, done={done}')
    env.render()
print(f"score: {score}")
"""



































