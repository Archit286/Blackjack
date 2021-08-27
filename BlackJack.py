import random

suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']
ranks = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
values = {'Ace': 11, 'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10}


class Card:
    def __init__(self, rank, suit):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return '{} of {}'.format(self.rank, self.suit)


class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in suits:
            for rank in ranks:
                card = Card(rank, suit)
                self.all_cards.append(card)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def getOne(self):
        return self.all_cards.pop()


class Player:
    def __init__(self):
        self.deck = []

    def add(self, card):
        self.deck.append(card)

    def view(self):
        for card in self.deck:
            print(card)
        print("Current Sum this Hand is ", self.sum())

    def sum(self):
        Sum = 0
        ace = 0
        for card in self.deck:
            if card.rank == 'Ace':
                ace += 1
            Sum += card.value
        flag = True
        while flag:
            if Sum > 21 and ace:
                Sum -= 10
                ace -= 1
            else:
                flag = False

        return Sum


def start():
    dealer = Player()
    player = Player()
    new_deck = Deck()
    new_deck.shuffle()
    for _ in range(2):
        dealer.add(new_deck.getOne())
        player.add(new_deck.getOne())
    print("Dealer's Card")
    print(dealer.deck[0])
    print("\n\nYour Cards")
    player.view()
    if dealer.sum() == 21 and player.sum() == 21:
        print('\n\nMatch Tied!!')
        return dealer, player
    elif dealer.sum() == 21:
        print("\n\nDealer got perfect 21")
        print('Dealer Won!!')
        return dealer, player
    elif player.sum() == 21:
        print("\n\nPlayer got perfect 21")
        print('Player Won!!')
        return dealer, player
    player_turn = True
    while player_turn:
        answer = ''
        while answer not in ['Hit', 'Stay']:
            answer = input('You want to Hit or Stay\n')
            if answer not in ['Hit', 'Stay']:
                print('Please Enter Hit or Stay')
        if answer == 'Hit':
            player.add(new_deck.getOne())
            player.view()
            if player.sum() == 21:
                print("\n\nPlayer got perfect 21")
                print("Player Wins!!")
                return dealer, player
            elif player.sum() > 21:
                print("\n\nPlayer got Busted")
                print("Dealer Wins!!")
                return dealer, player
        else:
            player_turn = False
    while dealer.sum() <= player.sum():
        dealer.add(new_deck.getOne())
    if dealer.sum() > 21:
        print("\n\nDealer got Busted")
        print("Player Wins")
        return dealer, player
    else:
        print("\n\nDealer Wins")
        return dealer, player


dealer, player = start()
print("\n\nFinal Hands of Player and Dealer:")
print("\n\nPlayer's Hand")
player.view()
print("\n\nDealer's Hand")
dealer.view()