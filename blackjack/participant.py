from hand import Hand

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

        for card in 
