# How does Black Jack work?
Yes Unfortunately I don't know how this game is played. I'll list how to game is played and I'll use that information to create the requirements for the environment.

## Abilities and Requirements of the Player
* Goal is to get the sum of the player's hand to 21.
    * If the sum goes over 21, the player busts
    * If the sum is less than 21, the player can win if his sum is greater than the sum of the dealer's hand.
    * If the sum is 21, the player wins
* Player has three actions
    * "hit": The player requests a card from the dealer to be added to his hand
        * After a "hit", the player must decide if he wants to "hit" again or "stay"
    * "stay": The player forfeits his turn to the other players and/or the dealer
    * "fold": The player forfeits the game and accepts the loss

## Abilities and Requirements of the Dealer
* Dealer is responsible for responding to the requests of the player
* Dealer begins a game by dealing 
    * 2 cards, face-up, to the player
    * 2 cards, one face-up and one face-down, to himself
* The dealer has 2 actions, but does not get to choose his actions:
    * Dealer must "stay" when his sum is greater than or equal to 17
    * Dealer must "hit" when his sum is less than or equal to 16

## Card Values
* Cards 2 through 10 are valued accordingly
* Face cards are valued at 10
* Ace
    * hard ace = 1
    * soft ace = 11

## Flow of a game
1. Dealer deals 2 cards, face-up, to the player
    * If the sum of these cards is 21, the player automatically wins
2. Dealer deasl 2 cards, one face-up and one face-down, to himself
3. The player decides to "hit" or "stand". 
    * If the player chooses to "hit" and does not "bust", the player must choose again to either "hit" or "stand"
4. Repeat 3 until player "busts" (player loses), achieves a sum of 21 (player wins), or player chooses to "stand"
5. Dealer reveals face-down card.
6. If the dealer's hand sums to 17 or greater, the dealer must "stand". Otherwise, the dealer must "hit" 
7. Repeat 6 until the dealer "stands" or "busts"
8. If this step is reached, both the player and the dealer are standing. The player/dealer who's hand's sum is closest to 21, wins.
