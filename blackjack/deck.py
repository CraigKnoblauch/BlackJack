from card import *
import random

def __init__(self):
    self.__two = Card('2', 2)
    self.__three = Card('3', 3)
    self.__four = Card('4', 4)
    self.__five = Card('5', 5)
    self.__six = Card('6', 6)
    self.__seven = Card('7', 7)
    self.__eight = Card('8', 8)
    self.__nine = Card('9', 9)
    self.__ten = Card('10', 10)
    self.__jack = Card('J', 10)
    self.__queen = Card('Q', 10)
    self.__king = Card('K', 10)

    self.__ace = # Crap, we need to be cognizant of a hand to do this

    # Make a deck of the cards
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

    self.__num_decks = 1

def getNumDecks(self):
    return self.__num_decks

def setNumDecks(self, num_decks):
    self.__num_decks = num_decks

def draw(self):
    return random.sample( self.__deck, 1 )
