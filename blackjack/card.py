from hand import Hand

class Card:

    def __init__(self, name, value, facedown=False):
        self.__name = name
        self.__value = value
        self.__facedown = facedown

    def getValue(self):
        return self.__value

    def getName(self):
        return self.__name

    def isFaceDown(self):
        return self.__facedown

    def setValue(self, value):
        self.__value = value

    def setName(self, name):
        self.__name = name

    def reveal(self):
        self.__facedown = False

    def flip(self):
        self.__facedown = not self.__facedown


def Ace(Card):

    def __init__(self, hand):
        Card.__init__('A', self.chooseValue(hand))

    def chooseValue(self, hand):
        # Even if an ace is the first in the hand, this will work.
        # Even if an ace follows, that ace will be counted as a 1
        if (hand.calculateSum() + 11) <= 21:
            self.__value = 11
        else:
            self.__value = 1
