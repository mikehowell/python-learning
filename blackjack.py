import random

suits = (
    chr(9825),
    chr(9826),
    chr(9824),
    chr(9827),
)  # the values are hearts, diamonds, spades, clubs
ranks = (
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Jack",
    "Queen",
    "King",
    "Ace",
)
values = {
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5,
    "Six": 6,
    "Seven": 7,
    "Eight": 8,
    "Nine": 9,
    "Ten": 10,
    "Jack": 10,
    "Queen": 10,
    "King": 10,
    "Ace": 11,
}

playing = True


class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + " of " + self.suit


class Deck:
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        deck_comp = ""  # start with an empty string
        for card in self.deck:
            deck_comp += "\n " + str(card)
        return "The deck has:" + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1


class Chips:
    def __init__(self, total=100):
        self.total = (
            total
        )  # This can be set to a default value or supplied by a user input
        self.bet = 0

    def win_bet(self):
        self.total += self.bet

    def lose_bet(self):
        self.total -= self.bet


def take_bet(chips):

    while True:
        try:
            chips.bet = int(input("Please enter an amount to bet: "))
        except ValueError:
            print(
                "You need to enter a valid whole number to place a bet\nPlease try again!"
            )
        else:
            if chips.bet > chips.total:
                print(
                    "You don't have enough to place this bet. Your current chips are {}".format(
                        chips.total
                    )
                )
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        turn = input("Would you like to Hit or Stand - press 'h' or 's': ")

        if turn[0].lower() == "h":
            hit(deck, hand)

        elif turn[0].lower() == "s":
            print("Player stands. Dealer is playing.")
            playing = False

        else:
            print("Sorry, please try again!")
            continue

        break


def show_some(player, dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print("", dealer.cards[1])
    print("\nPlayer's Hand:", *player.cards, sep="\n ")


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep="\n ")
    print("Dealer's Hand =", dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep="\n ")
    print("Player's Hand =", player.value)


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer):
    print("Dealer and Player tie! It's a push.")


def play_blackjack():
    global playing
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
        player_chips = Chips()

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(blackjack_deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

            # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(blackjack_deck, dealer_hand)

            # Show all cards
            show_all(player_hand, dealer_hand)

            # Run different winning scenarios
            if dealer_hand.value > 21:
                dealer_busts(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value > player_hand.value:
                dealer_wins(player_hand, dealer_hand, player_chips)

            elif dealer_hand.value < player_hand.value:
                player_wins(player_hand, dealer_hand, player_chips)

            else:
                push(player_hand, dealer_hand)

        # Inform Player of their chips total
        print("\nPlayer's winnings stand at", player_chips.total)

        # Ask to play again
        new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
        if new_game[0].lower() == "y":
            playing = True
            continue
        else:
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    play_blackjack()
