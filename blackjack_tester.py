from blackjack import BlackJack
import random
import time

raymond = BlackJack()

i = 1
while True:
    print("-----------------------\nGame " + str(i) + "\n-----------------------\n")
    done = False
    while not done:
        action = random.randint(0, 1)
        raymond.render()
        state, reward, done, _ = raymond.step(action)
        raymond.render()
        time.sleep(1)

    if reward > 0:
        print("Raymond Wins")
    else:
        print("Dealer Wins")

    i += 1
    raymond.reset()
