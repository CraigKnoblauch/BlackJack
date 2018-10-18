from blackjack import BlackJack
from agent import DQNAgent
import os
import numpy as np

env = BlackJack()
raymond = DQNAgent(2, env.action_space.n)

# Set hyper parameters
state_size = 2
action_size = env.action_space.n
batch_size = 32 # For gradient descent, vary by powers of 2
n_episodes = 1000
out_dir = 'model_output/raymond'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

with open('training.txt', 'w') as f:
    pass

for e in range(n_episodes):
    turn_counter = 0
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False

    while not done:
        env.render()
        action = raymond.act(state)
        next_state, reward, done, _ = env.step(action)

        next_state = np.reshape(next_state, [1, state_size])
        raymond.remember(state, action, reward, next_state, done)

        state = next_state
        turn_counter += 1

    with open('training.txt', 'a') as f:
        f.write('Episode {}/{}, Score: {}, e:{:.2}'.format(e, n_episodes, turn_counter, raymond.epsilon))

    # Sample mem, replay experiences, train theta
    if len(raymond.memory) > batch_size:
        raymond.replay(batch_size)

    if reward < 0:
        winner = "Dealer"
    else:
        winner = "Raymond"

    print("Episode {} Winner {}".format(e, winner))

    if e % 20 == 0:
        raymond.save(out_dir + 'weights_' + '{:04d}'.format(e) + "hdf5")




