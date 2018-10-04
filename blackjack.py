import gym
from gym import spaces
from gym.utils import seeding 
import random

## 
# Defining the deck in this way will allow us to render easily
# and will provide and "infinite" deck
deck = {'1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        'J': 10,
        'Q': 10,
        'K': 10,
        'A': 0,
        'A1': 1,
        'A11': 11
       }

##
# Since the ace can take on multiple values, this class allows us to organize the duality
class Ace():

    def __init__(self, val):
        self.value = val

    def getValue(self):
        return self.value

    def setValue(self, val):
        self.value = val

    # Chooses an appropriate value for an ace, based on the current hand
    def chooseValue(self, hand):
        val = 1

        # Sum the hand thus far
        hand_sum = 0
        for deck_key in hand:
            hand_sum += deck[deck_key]

        # Determine the value of ace that will prevent the holder from busting. If no such value exists, value remains at 1
        if (hand_sum + 11) <= 21:
            val = 11

        return val

        

# Closest I can get to #define
STAY = 0
HIT = 1


## "Private" functions
# Any functions that I want the class to have access to, but that I don't
# want callers of the API to have access to, should be put into this secion.
# You know, Python is exceedingly dumb for OO tasks



## ------------------------------------------------------------------------------------#

class BlackJack(gym.Env):

    def __init__(self):
        # Init the player and the dealer's hand
        player_hand = random.sample( list(deck), 2 ) 
        dealer_hand = random.sample( list(deck), 2 ) 

        player_sum = self.getSum(player_hand)
        dealer_sum = self.getSum(dealer_hand)

        # I need a way to track if the dealer has flipped over his card
        # To do this, the first position of the dealer's hand will be used 
        # to indicate. If index 0 of the dealer's hand is 0, he as not flipped
        # his card, if it is < 0, he has. This assures the sum function cannot confuse
        # the object in the first postion with a card.
        (dealer_hand).insert(0, 0)

        self.action_space = spaces.Discrete(2) # 0 is stay, 1 is hit
        self.observation_space = [player_hand,
                                  player_sum,
                                  dealer_hand,
                                  dealer_sum
                                  ]

        self.observation = self.observation_space # I think my observation understanding is breaking down

        self.render()
        self.seed() # Based on other space src I've seen you need this

    def step(self, action):
        # Step returns observation, reward, done, info dict

        # Default reward is 0
        reward = 0

        # Recall this is a discrete action space where 0 means "stay" and 1 means "hit"
        if action == HIT:
            self.giveCardToPlayer()
            if self.isBust( self.getPlayerHand() ):
                self.updatePlayerSum()
                done = True
                reward = -10
            else:
                done = False

        if action == STAY:
            # Flip the dealer's card and update his sum
            self.revealDealerCard()
            self.updateDealerSum()
            while not self.isBust( self.getDealerHand() ) and self.getDealerSum() <= 16:
                self.giveCardToDealer()
                self.updateDealerSum()

            # Dealer is staying
            done = True

            if self.isBust( self.getDealerHand() ):
                # Player wins
                reward = 10
            
            if self.getDealerSum() == 21:
                # Player loses, a possible tie doesn't matter
                reward = -10

            if self.getDealerSum() >= self.getPlayerSum():
                # Dealer wins, even in ties
                reward = -10
            else:
                # Player wins
                reward = 10

        return self.observation, reward, done, {}

    def isBust(self, hand):
        bust = False
        hand_sum = self.getSum(hand)

        if hand_sum > 0: # This is a valid hand, dealer or player
            bust = (hand_sum > 21)
        else: # The dealer hasn't shown his card, why has the program gotten here?!?! give a massive error
            bust = "ERROR: isBust, Dealer hasn't shown his card"

        return bust
    
    def giveCardToPlayer(self):
        card = random.sample( list(deck), 1 )
        # Determine if card is an ace. If it is, determine and set its value, based on the current sum of the hand
        if card == 'A':
            ace_obj = Ace(0)
            val_of_ace = ace_obj.chooseValue( self.getPlayerHand() )
            if val_of_ace == 1:
                card = 'A1'
            else:
                card = 'A11'

        ( (self.observation)[0] ).append( card )

    def giveCardToDealer(self):
        ( (self.observation)[2] ).append( random.sample( list(deck[:-2]), 1 ) )

    def updatePlayerSum(self):
        ( (self.observation)[1] ) = self.getSum(self.getPlayerHand())

    def updateDealerSum(self):
        ( (self.observation)[3] ) = self.getSum(self.getDealerHand())

    def revealDealerCard(self):
        ( (self.observation)[2] )[0] = -1

    def getPlayerHand(self):
        return (self.observation)[0]

    def getDealerHand(self):
        return (self.observation)[2]

    def getPlayerSum(self):
        return (self.observation)[1]

    def getDealerSum(self):
        return (self.observation)[3]

    # TODO: ISSUE (does not account for aces)
    def getSum(self, hand):
        hand_sum = 0

        if isinstance(hand, int): # Dealer's hand
            if hand[0] == 0: # Dealer's card is not showing
                hand_sum = -1
            else:
                for deck_key in hand[1:]: # sum the dealer's hand
                    hand_sum += deck[ deck_key ]
        else: # Player's hand
            for deck_key in hand: # sum the player's hand
                hand_sum += deck[ deck_key ]
    
        return hand_sum

    def render(self):
        dealer_str = "Dealer ("
        dealer_sum = self.getDealerSum()

        player_str = "Player ("
        player_sum = self.getPlayerSum()

        # Construct dealer string
        if dealer_sum < 0: # Dealer's hand is not showing
            dealer_str += "): "
        else:
            dealer_str += str(dealer_sum)
            dealer_str += "): "

        for deck_key in self.getDealerHand():
            dealer_str += str(deck_key) 
            dealer_str += " "

        # Construct player string
        player_str += str(player_sum)
        player_str += "): "
        for deck_key in self.getPlayerHand():
            player_str += str(deck_key)
            player_str += " "

        # Render
        print(dealer_str)
        print(player_str)
        print("")

    # Taken from the various environments available at github.com/openai/gym
    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def reset(self):
        # Init the player and the dealer's hand
        player_hand = random.sample( list(deck), 2 ) 
        dealer_hand = random.sample( list(deck), 2 ) 

        player_sum = self.getSum(player_hand)
        dealer_sum = self.getSum(dealer_hand)

        # I need a way to track if the dealer has flipped over his card
        # To do this, the first position of the dealer's hand will be used 
        # to indicate. If index 0 of the dealer's hand is 0, he as not flipped
        # his card, if it is < 0, he has. This assures the sum function cannot confuse
        # the object in the first postion with a card.
        (dealer_hand).insert(0, 0)

        self.action_space = spaces.Discrete(2) # 0 is stay, 1 is hit
        self.observation_space = [player_hand,
                                  player_sum,
                                  dealer_hand,
                                  dealer_sum
                                  ]

        self.observation = self.observation_space # I think my observation understanding is breaking down

        

    
