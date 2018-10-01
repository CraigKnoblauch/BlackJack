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
3. The player decides to "hit" or "stay". 
    * If the player chooses to "hit" and does not "bust", the player must choose again to either "hit" or "stay"
4. Repeat 3 until player "busts" (player loses), achieves a sum of 21 (player wins), or player chooses to "stay"
5. Dealer reveals face-down card.
6. If the dealer's hand sums to 17 or greater, the dealer must "stay". Otherwise, the dealer must "hit" 
7. Repeat 6 until the dealer "stays" or "busts"
8. If this step is reached, both the player and the dealer are staying. The player/dealer who's hand's sum is closest to 21, wins.

# Black Jack environment
* Inherit gym.env

## What will the render look like?
* X will represent a face-down card
```
Dealer(): A, X
Player(12): 4, 8
```
## What are the actions?
`["stay", "hit"]`

### How will the action space be defined?
This is a discrete action space constrained to 2 possibilites. We should be able to simply call the spaces API
```
action_space = spaces.Discrete(2)
```
0 for stay, 1 for hit

## What is the state definition?
Note that the second element of `dealer_hand_list` is not known until the end of the player's turn
```
[<player_hand_list>, <player_hand_sum>, <dealer_hand_list>, <dealer_hand_sum>]
``` 
Even though, in a real game, the deck would shrink, I'm assuming an *infinite* deck. This way I don't have to account for this in the state space. It may be a worthwile TODO though.

### How will the state space be defined?
I took a look at the `spaces` src. I feel confident that I would be able to replicate a space without having to use one of their spaces. This would work out best for me, because gym doesn't have a space that fits this definition nicely.

## What is/are the end condition(s)?
* Player reaches a sum of 21                                  --> WIN
* Player reaches a sum > 21                                   --> LOSS 
* Player's sum is < 21 'AND' Player's sum is > dealer's sum   --> WIN
* Player's sum is < 21 'AND' Player's sum is < dealer's sum   --> LOSS
* Player's sum is == dealer's sum                             --> LOSS
    * Technically this is a tie, for simplicity, it's labeled as a LOSS here

## What is the reward structure?
We'll do a simple reward structure. 
* +10 for winning
* -10 for losing
There's the oppurtunity to make this more complicated with the addition of betting 
