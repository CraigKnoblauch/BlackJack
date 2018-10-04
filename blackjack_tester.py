from blackjack import BlackJack
import random
import time

bj = BlackJack()

i = 1
while True:
    print("-----------------------\nGame " + str(i) + "-----------------------\n")
    done = False
    while not done:
        action = random.randint(0, 1)
        bj.render()
        state, reward, done, _ = bj.step(action)
        time.sleep(2)
    i += 1
