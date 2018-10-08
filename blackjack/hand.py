from card import Card

# Ugh, doing a game='blackjack' is a really bad way of doing this
class Hand:

    def __init__(self, cards):
        """
        A hand must start with a list of cards
        """
        self.__cards = cards
        self.__quality = self.determineQuality() # if quality is < 0, quality is unknown

    def addCard(self, card):
        (self.__cards).append(card)
        self.updateQuality()

    def determineQuality(self, game='blackjack'):
        if game == 'blackjack':
            quality = self.blackjackSum()

        return quality

    def updateQuality(self):
        self.__quality = self.determineQuality(game='blackjack')

    def getQuality(self):
        return self.__quality

    # Theory here is that if you try to loop through an object, you'll loop through the cards
    def __iter__:
        return self.__cards

    def blackjackSum(self):
        total = 0
        for i, card in enumerate(self.__cards):
            if card.isFaceDown():
                total = -1
                break
            else:
                if card.getName() == '1':
                    total += 1
                else if card.getName() == '2':
                    total += 2
                else if card.getName() == '3':
                    total += 3
                else if card.getName() == '4':
                    total += 4
                else if card.getName() == '5':
                    total += 5
                else if card.getName() == '6':
                    total += 6
                else if card.getName() == '7':
                    total += 7
                else if card.getName() == '8':
                    total += 8
                else if card.getName() == '9':
                    total += 9
                else if card.getName() == '10' or card.getName() == 'J' or card.getName() == 'Q' or card.getName() == 'K':
                    total += 10
                else: # This is an ace
                    total += self.blackjackAceValue(total)

    def blackjackAceValue(self, total):
        value = 1
        if total + 11 <= 21
            value = 11

        return value

