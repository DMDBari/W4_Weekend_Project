import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.suit_symbols = {'Hearts': '\u2665', 'Diamonds': '\u2666', 'Clubs': '\u2663', 'Spades': '\u2660'}

    def show(self):
        print( f"{self.rank:<2}{self.suit}")

class Deck:
    def __init__(self):
        self.cards = []
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        suits= ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(rank, suit))

    def deal(self, player):
        card = self.cards.pop()
        player.hand.append(card)

class Player:
    def __init__(self):
        self.hand = []

    def calculate_hand(self):
        value = 0
        for card in self.hand:
            if card.rank in ['J', 'Q', 'K']:
                value += 10
            elif card.rank == 'A':
                value += 11 if value <= 10 else 1
            else:
                value += int(card.rank)
        return value

class Dealer(Player):
    def should_hit(self):
        return self.calculate_hand() < 17


playing = True
while playing:
    deck = Deck()
    random.shuffle(deck.cards)

    player = Player()
    dealer = Dealer()

    for _ in range(2):
        deck.deal(player)
        deck.deal(dealer)

    while True:
        print("Your hand:")
        for card in player.hand:
            card.show()
        if player.calculate_hand() > 21:
            print("You bust! The dealer wins.")
            break
        should_continue = input("Would you like to hit or stand? (h/s): ")
        if should_continue.lower().strip() == "h":
            deck.deal(player)
        else:
            break

    if player.calculate_hand() <= 21:
        while dealer.should_hit():
            deck.deal(dealer)
        print("Dealer's hand:")
        for card in dealer.hand:
            card.show()
        if dealer.calculate_hand() > 21:
            print("The Dealer Busts! You Win!")
        elif dealer.calculate_hand() < player.calculate_hand():
            print("You are closer to 21! You Win!")
        elif dealer.calculate_hand() > player.calculate_hand():
            print("The Dealer wins!")
        else:
            print("It's a tie")
    

    play_again = input("Would you like to play another round? (y/n): ")
    if play_again.lower().strip() != "y":
        playing = False