import gym
from gym import spaces
from gym.utils import seeding 
from cardgames.table import Table
from cardgames.card import Card
from cardgames.deck import Deck
from cardgames.participant import *
from cardgames.hand import Hand

STAY = 0
HIT = 1

class BlackJack(gym.Env):

    def __init__(self):
        self.__table = Table('blackjack')
        self.action_space = spaces.Discrete(2) # 0 for stay, 1 for hit
        self.__dealer = (self.__table).getDealer()
        self.__player = (self.__table).getPlayer(0)

        self.observation_space = [ (self.__player).getHand().getQuality(),
                                   (self.__dealer).getHand().getQuality() ]
        
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
            self.__updatePlayerState( (self.__player).getHand().getQuality() )
            done = self.__isBust( (self.__player).getHand() )
            if done:
                reward = -10

        if (not done) and (action == STAY): # Time for the dealer to go
            # Flip the first card
            (self.__dealer).getHand().flipCard(0)

            (self.__dealer).getHand().updateQuality()
                
            # Dealer must hit when hand quality is less than 17
            while (self.__dealer).getHand().getQuality() < 17:
                card = (self.__dealer).deal()
                (self.__dealer).getHand().addCard(card)
                self.__updateDealerState( (self.__dealer).getHand().getQuality() )
                if self.__isBust( (self.__dealer).getHand() ):
                    done = True
                    reward = 10

            # Compare the qualities of the dealer and the player
            if not done:
                if (self.__player).getHand().getQuality() <= (self.__dealer).getHand().getQuality(): 
                    # Dealer wins when hand is grater or tied
                    reward = -10
                else:
                    # Player wins when hand quality is greater than dealer's
                    reward = 10

            done = True

        # The player has hit, and not bust
        if not done:
            reward = 10

        return self.observation_space, done, reward, {}

    
    def render(self):
        print( (self.__dealer).getRender() )
        print( (self.__player).getRender() )

    def reset(self):
        self.__table = Table('blackjack')
        self.action_space = spaces.Discrete(2) # 0 for stay, 1 for hit
        self.__dealer = (self.__table).getDealer()
        self.__player = (self.__table).getPlayer(0)

        self.observation_space = [ (self.__player).getHand().getQuality(),
                                   (self.__dealer).getHand().getQuality() ]
        
        self.seed() # Based on other space src I've seen you need this

    # Taken from the various environments available at github.com/openai/gym
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def getTable(self):
        return self.__table

        

    
