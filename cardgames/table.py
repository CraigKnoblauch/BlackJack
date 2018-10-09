from cardgames import deck
from cardgames import card
from cardgames import hand
from cardgames import participant

class Table:

    def __init__(self, game):
        self.__game = game

        if game == 'blackjack':

            self.__deck = deck.Deck() # Assuming 1, infinite deck

            # Make a hand for the player
            player_hand = self.__blackjackPlayerHand()
            self.__players = [participant.Player(player_hand)]  # Start with one player
            
            # Make a hand for the dealer
            dealer_hand = self.__blackjackDealerHand()
            self.__dealer = participant.Dealer( dealer_hand )

        else:
            # TODO: idk, throw a not supported arg or something
            pass

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
        
    def getGame(self):
        return self.__game
    
    def setGame(self, game):
        self.__game = game

    def __blackjackPlayerHand(self):
        """ Get two cards, give them as a hand to the player """
        cards = []
        cards.append( (self.__deck).draw() )
        cards.append( (self.__deck).draw() )

        return hand.Hand(cards, self.__game)

    def __blackjackDealerHand(self):
        """
        Get two cards, one of them face down, give them to the dealer
        """
        cards = []
        cards.append( (self.__deck).draw() )
        cards.append( (self.__deck).draw() )
        (cards[0]).flip()

        return hand.Hand(cards, self.__game)

    