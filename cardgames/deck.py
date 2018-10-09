from cardgames import card
import random

class Deck():

    def __init__(self, num_decks=1, infinite=True):
        self.__two = card.Card('2')
        self.__three = card.Card('3')
        self.__four = card.Card('4')
        self.__five = card.Card('5')
        self.__six = card.Card('6')
        self.__seven = card.Card('7')
        self.__eight = card.Card('8')
        self.__nine = card.Card('9')
        self.__ten = card.Card('10')
        self.__jack = card.Card('J')
        self.__queen = card.Card('Q')
        self.__king = card.Card('K')
        self.__ace = card.Card('A')

        # Make a deck of the card.Cards
        self.__deck = [ self.__two, self.__two, self.__two, self.__two,
                        self.__three, self.__three, self.__three, self.__three,
                        self.__four, self.__four, self.__four, self.__four,
                        self.__five, self.__five, self.__five, self.__five,
                        self.__six, self.__six, self.__six, self.__six,
                        self.__seven, self.__seven, self.__seven, self.__seven,
                        self.__eight, self.__eight, self.__eight, self.__eight,
                        self.__nine, self.__nine, self.__nine, self.__nine,
                        self.__ten, self.__ten, self.__ten, self.__ten,
                        self.__jack, self.__jack, self.__jack, self.__jack,
                        self.__jack, self.__jack, self.__jack, self.__jack,
                        self.__king, self.__king, self.__king, self.__king,
                        self.__ace, self.__ace, self.__ace, self.__ace ]

        self.__num_decks = num_decks
        self.__infinite = infinite

    def draw(self):
        if self.__infinite:
            drawn = random.sample( self.__deck, 1 )
        else:
            drawn = (self.__deck).pop() # TODO: implement support for this

        return drawn

    def shuffle(self):
        random.shuffle( self.__deck )

    def getDeck(self):
        return self.__deck

    def getNumDecks(self):
        return self.__num_decks

    def setNumDecks(self, num_decks):
        self.__num_decks = num_decks

    def isInfinite(self):
        return self.__infinite

    def setInfinite(self, infinite):
        self.__infinite = infinite
