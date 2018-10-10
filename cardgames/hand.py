from cardgames import card

# Ugh, doing a game='blackjack' is a really bad way of doing this
class Hand:

    def __init__(self, cards, game):
        """
        A hand must start with a list of cards
        """
        self.__cards = cards
        self.__game = game
        self.__quality = self.determineQuality() # if quality is < 0, quality is unknown

    def addCard(self, card):
        (self.__cards).append(card)
        self.updateQuality()

    def getCards(self):
        return self.__cards

    def setCards(self, cards):
        self.__cards = cards

    def flipCard(self, cardi):
        ( (self.__cards)[cardi] ).flip()

    def determineQuality(self):
        if self.__game == 'blackjack':
            quality = self.__blackjackSum()

        return quality

    def updateQuality(self):
        self.__quality = self.determineQuality()

    def getQuality(self):
        return self.__quality

    # Theory here is that if you try to loop through an object, you'll loop through the cards
    def __iter__(self):
        self.cardi = 0
        return self

    def __next__(self):
        cardi = self.cardi

        if cardi >= len(self.__cards):
            raise StopIteration

        self.cardi = cardi + 1

        return (self.__cards)[cardi]

    def __blackjackSum(self):
        total = 0
        for i, card in enumerate(self.__cards):
            if card.isFaceDown():
                total = -1
                break
            else:
                if card.getName() == '1':
                    total += 1
                elif card.getName() == '2':
                    total += 2
                elif card.getName() == '3':
                    total += 3
                elif card.getName() == '4':
                    total += 4
                elif card.getName() == '5':
                    total += 5
                elif card.getName() == '6':
                    total += 6
                elif card.getName() == '7':
                    total += 7
                elif card.getName() == '8':
                    total += 8
                elif card.getName() == '9':
                    total += 9
                elif card.getName() == '10' or card.getName() == 'J' or card.getName() == 'Q' or card.getName() == 'K':
                    total += 10
                else: # This is an ace
                    total += self.__blackjackAceValue(total)

        return total

    def __blackjackAceValue(self, total):
        value = 1
        if total + 11 <= 21:
            value = 11

        return value
