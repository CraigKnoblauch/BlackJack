import Deck
from participant import *

class Table:

    def __init__(self, game):
        self.__deck = Deck()
        self.__dealer = Dealer()

        if game == 'blackjack':
            self.__players = [Player()] # Start with one player
        else:
            # TODO: idk, throw a not supported arg or something

    def getDeck(self):
        return self.__deck

    def getDealer(self):
        return self.__dealer

    def getPlayers(self):
        return self.__players

    def getPlayer(self, p):
        return (self.__players)[p]

    def addPlayer(self, player):
        (self.__players).append(player)
