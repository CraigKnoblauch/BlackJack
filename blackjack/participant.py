from hand import Hand
import Deck
import Card

class Participant():

    def __init__(self, hand):
        self.__hand = hand

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
        self.__deck = Deck() # TODO this is bad design, I'd like to give the dealer a table but that doesn't make sense in context of the larger design

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
