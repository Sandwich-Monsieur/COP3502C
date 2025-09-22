#Project 1: Blackjack

import p1_random as p1
rng = p1.P1Random()
#import the module (do this on the first line of code)
#create a P1Random variable
#my_number = rng.next_int(10) #Yields a random number in range [0, 9]

#my_number = rng.next_int(13) + 1 #Yields a random number in range [1, 13]
#my_value = rng.next_int(11) + 16 #Yields a random number in range [16,26]



def deal_card(card, hand):
    global player_hand
    card = rng.next_int(13) + 1
    player_hand += add_card(card)
    print(f"Your card is a {check_card(card)}!")
    print(f"Your hand is: {player_hand}")
    print()

def check_card(card):
    if card == 1:
        return "ACE"
    if card == 11:
        return "JACK"
    if card == 12:
        return "QUEEN"
    if card == 13:
        return "KING"
    else:
        return card

def add_card(card):
    if card == 11:
        return 10
    if card == 12:
        return 10
    if card == 13:
        return 10
    else:
        return card

def dealer():
    hand = rng.next_int(11) + 16
    return hand

def options():
    global wins
    global losses
    global ties
    global games
    global card
    global player_hand
    global play
    while True:
        print('1. Get another card')
        print('2. Hold hand')
        print('3. Print statistics')
        print('4. Exit')
        print()
        choice = int(input("Choose an option: "))
        print()
        if choice == 1:
            deal_card(card, player_hand)
            if player_hand >= 21:
                if player_hand > 21:
                    print("You exceeded 21! You lose.\n")
                    losses += 1
                if player_hand == 21:
                    print("BLACKJACK! You win!\n")
                    wins += 1
                player_hand = 0
                break
        if choice == 2:
            dealer_hand = dealer()
            print("Dealer's hand:", dealer_hand)
            print("Your hand is:", player_hand)
            print()
            if (player_hand <= 21 and dealer_hand <= 21):
                if player_hand > dealer_hand:
                    print("You win!\n")
                    wins += 1
                if player_hand < dealer_hand:
                    print("Dealer wins!\n")
                    losses += 1
                if (player_hand == dealer_hand):
                    print("It's a tie! No one wins!\n")
                    ties += 1
            elif (dealer_hand > 21):
                print("You win!\n")
                wins += 1
            elif (dealer_hand == 21 and dealer_hand > player_hand):
                print("Dealer wins!\n")
                losses += 1
            player_hand = 0
            break
        if choice == 3:
            percent = 100 * wins / (games - 1)
            print("Number of Player wins:", wins)
            print("Number of Dealer wins:", losses)
            print("Number of tie games:", ties)
            print("Total # of games played is:", games - 1)
            print(f"Percentage of Player wins: {percent:.1f}%")
        if choice == 4:
            play = False
            break
        if choice != 1 and choice != 2 and choice != 3 and choice != 4:
            print("Invalid input!\n\nPlease enter an integer value between 1 and 4.")


wins = 0
losses = 0
ties = 0
games = 1
card = 0
player_hand = 0
play = True
while play:
    print(f"START GAME #{games}")
    print()
    deal_card(card, player_hand)
    options()
    games += 1