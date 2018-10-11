from cardgames import card
import random

class Deck:

    def __init__(self, num_decks=1, infinite=True):
        self.__num_decks = num_decks
        self.__infinite = infinite

        # We're going to make a list of seperate card objects.
        self.__cardnames = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']

        self.__deck = self.__makeDeck()

        if not self.__infinite:
            if self.__num_decks > 1:
                for _ in range(self.__num_decks - 1):
                    (self.__deck).extend(self.__makeDeck())

        # Shuffle the deck before it's used
        self.shuffle()
        
    def __makeDeck(self):
        """ Make and return a deck of 52 unique cards """
        deck = []
        for cardname in self.__cardnames:
            i = 0
            while i < 4:
                deck.append(card.Card(cardname))
                i += 1

        return deck

    def draw(self):
        # Bear in mind tha this has a chance of returning a card that has already been drawn
        if self.__infinite:
            drawn = random.choice(self.__deck)
        else:
            drawn = (self.__deck).pop() # TODO: Currently no way to replenish the deck

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
