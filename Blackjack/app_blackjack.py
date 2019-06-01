from card import Card
from suits import suits
from ranks import ranks
from values import values
from deck import Deck
from hands import Hand
from chips import Chips
from helper_functions import *

global_playing = True
global_chips = 0


def play_blackjack():
    global global_playing
    global global_chips

    while True:
        # Print an opening statement
        print("Welcome to Black Jack!")

        # Create & shuffle the deck, deal two cards to each player
        blackjack_deck = Deck()
        blackjack_deck.shuffle()

        player_hand = Hand()
        dealer_hand = Hand()

        for i in range(2):
            player_hand.add_card(blackjack_deck.deal())
            dealer_hand.add_card(blackjack_deck.deal())

        # Set up the Player's chips
        if global_chips == 0:
            while True:
                try:
                    chip_value = int(
                        input("How much money would you like to convert to chips? ")
                    )
                    global_chips = Chips(chip_value)
                except ValueError:
                    print("Please enter a whole number: ")
                else:
                    # Prompt the Player for their bet
                    take_bet(global_chips)
                    break
        else:
            # Prompt the Player for their bet
            take_bet(global_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while (
            global_playing and global_playing >= 0
        ):  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(blackjack_deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, global_chips)
                break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(blackjack_deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, global_chips)
                break

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, global_chips)
                break

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, global_chips)
                break

            else:
                push(player_hand, dealer_hand)
                break

        # Inform Player of their chips total
        print("\nPlayer's winnings stand at", global_chips.total)

        # Ask to play again
        while True:
            new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
            if new_game[0].lower() == "y":
                global_playing = True
                break
            elif new_game[0].lower() == "n":
                global_playing = False
                break
            else:
                print("Please choose 'y' or 'n' to continue.")
                continue

        if not global_playing:
            print("Thanks for playing")
            break


if __name__ == "__main__":
    play_blackjack()
