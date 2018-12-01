from blackjack import BlackJack
from agent import DQNAgent
import os
import numpy as np
import matplotlib.pyplot as plt

GROUP_SIZE = 20

class RaymondReport:

    def __init__(self):
        self.performance_data = []

    def updatePerformance(self, perf):
        self.performance_data.append(perf)

    def graphPerformance(self, fname='performance.png'):
        x = [i+1 for i in range(len(self.performance_data))]
        plt.plot(x, self.performance_data)
        plt.title("Raymonds performance per group of {} games".format(GROUP_SIZE))
        plt.xlabel("Groups of {} games".format(GROUP_SIZE))
        plt.ylabel("Win Rate %")
        plt.savefig(fname)


env = BlackJack()
raymond = DQNAgent(2, env.action_space.n, learning_rate=0.0001, epsilon=0.9995)
report = RaymondReport()

# Set hyper parameters
state_size = 2
action_size = env.action_space.n
batch_size = 32 # For gradient descent, vary by powers of 2
n_episodes = 10000
out_dir = 'model_output/raymond'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

with open('training.txt', 'w') as f:
    pass

with open('training.csv', 'w') as f:
    pass

raymond_score = 0 # Increment each time raymond wins. Will plot wins against time

for e in range(n_episodes):
    state = env.reset()
    state = np.reshape(state, [1, state_size])
    done = False

    while not done:
        # env.render()
        action = raymond.act(state)
        next_state, reward, done, _ = env.step(action)

        next_state = np.reshape(next_state, [1, state_size])
        raymond.remember(state, action, reward, next_state, done)

        state = next_state

    if reward < 0:
        winner = "Dealer"
    else:
        winner = "Raymond"
        raymond_score += 1

    with open('training.txt', 'a') as f:
        f.write('Episode {}/{}, Winner: {}, e:{:.2}'.format(e, n_episodes, winner, raymond.epsilon))
        f.write('\n')

    # Sample mem, replay experiences, train theta
    if len(raymond.memory) > batch_size:
        raymond.replay(batch_size)

    print("Episode {}/{} Winner {}".format(e, n_episodes, winner))

    if e % GROUP_SIZE == 0:
        raymond.save(out_dir + 'weights_' + '{:04d}'.format(e) + "hdf5")

        report.updatePerformance(raymond_score/GROUP_SIZE)

        raymond_score = 0

report.graphPerformance()




