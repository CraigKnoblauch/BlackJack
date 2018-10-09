import gym
from gym import spaces
from gym.utils import seeding 
from cardgames.table import Table

STAY = 0
HIT = 1

class BlackJack(gym.Env):

    def __init__(self):
        self.__table = Table('blackjack')
        self.action_space = spaces.Discrete(2) # 0 for stay, 1 for hit
        self.__dealer = (self.__table).getDealer()
        self.__player = (self.__table).getPlayer()

        self.observation_space = [ (self.__player).getHand().getQuality(),
                                   (self.__dealer).getHand().getQuality() ]

        self.reward = 0
        
        self.seed() # Based on other space src I've seen you need this

    def __isBust(self, hand):
        return hand.getQuality() > 21

    def __updatePlayerState(self, quality):
        (self.observation_space)[0] = quality

    def __updateDealerState(self, quality):
        (self.observation_space)[1] = quality

    def step(self, action):
        done = False

        if action == HIT:
            card = (self.__dealer).deal()
            (self.__player).getHand().addCard(card)
            done = self.__isBust( (self.__player).getHand() )

        if (not done) and (action == STAY): # Time for the dealer to go
            




    # Taken from the various environments available at github.com/openai/gym
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

        

    
