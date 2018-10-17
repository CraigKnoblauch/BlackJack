import tensorflow as tf
from tensorflow.contrib.layers import fully_connected
from collections import deque, Counter
import gym
from blackjack import BlackJack
import numpy as np
import random
from datetime import datetime

env = BlackJack()
n_outputs = env.action_space.n

## Build the Q network
def q_network(state, name_scope):
    pass

epsilon = 0.5
eps_min = 0.05
eps_max = 1.0
eps_decay_steps = 500000

def e_greedy(action, step):
    p = np.random.random(1).squeeze()
    avge = eps_max - (eps_max-eps_min) * step/eps_decay_steps
    epsilon = max(eps_min, avge)


# Init the experience replay buffer
buffer_len = 20000
exp_buffer = deque(maxlen=buffer_len)

def sample_memories(batch_size):
    perm_batch = np.ranoom.permutation(len(exp_buffer))[:batch_size]
    mem = np.array(exp_buffer)[perm_batch]
    return mem[:,0], mem[:,1], mem[:,2], mem[:,3], mem[4,:]


# Network hyper-parameters
num_episodes = 1000
batch_size = 48
input_shape = UNKNOWN
learning_rate = 0.001
state_shape = UNKNOWN
discount_factor = 0.97

global_step = 0
copy_steps = 100
steps_train = 4
start_steps = 2000

logdir = 'logs'

tf.reset_default_graph()





