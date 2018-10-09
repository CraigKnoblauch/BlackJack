from abc import ABC, abstractmethod

from cardgames import hand
from cardgames import deck
from cardgames import card

class Participant(ABC):

    def __init__(self, hand):
        self.__hand = hand
        ABC.__init__()

    def getHand(self):
        return self.__hand

    def setHand(self, hand):
        self.__hand = hand

    @abstractmethod
    def getRender(self):
        pass

class Player(Participant):

    def __init__(self, hand):
        Participant.__init__(hand)

    def getRender(self):
        player_str = "Player ("

        # If the quality is known, add it to the render
        quality = (self.__hand).getQuality()
        if quality >= 0:
            player_str += str(quality)

        player_str += "): "

        for card in self.__hand:
            if card.isFaceDown():
                player_str += "X "
            else:
                player_str += (card.getName() + ' ')

        print(player_str)

class Dealer(Participant):

    def __init__(self, hand):
        Participant.__init__(hand)
        self.__deck = deck.Deck()

    def getRender(self):
        dealer_str = "Dealer ("

        # If the quality is known, add it to the render
        quality = (self.__hand).getQuality()
        if quality >= 0:
            dealer_str += str(quality)

        dealer_str += "): "

        for card in self.__hand:
            if card.isFaceDown():
                dealer_str += "X "
            else:
                dealer_str += (card.getName() + ' ')

        print(dealer_str)

    def deal(self):
        return (self.__deck).draw()
