class Card:

    def __init__(self, name, facedown=False):
        self.__name = name
        self.__facedown = facedown

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def isFaceDown(self):
        return self.__facedown

    def flip(self):
        self.__facedown = not self.__facedown