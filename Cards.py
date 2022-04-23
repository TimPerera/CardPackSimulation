# the first part is to create a simulation for a deck of cards. 
# therefore we need 52 cards (without jokers)


# behaviours we want to be able to simulate 
# ** Cards **
# shuffle,serve

# ** Player **
# draw, peek, burn 

# TODO: Account for card distributions when the card pack runs out.
# TODO: Add documentation
# TODO: Push to Git
# TODO: Add tests


import random


class Card():
    def __init__(self,val,suit):
        self.card = (val,suit)
        self.val = val
        self.suit = suit

    def show_card(self):
        return f'{self.card[0]} of {self.card[1]}'


class Deck(Card):
    def __init__(self, cards=[]):
        self.cards = cards
        self.build()

    def build(self):
        # Compile the list of cards in a deck
        card_vals = ['1','2','3','4','5','6','7','8','9','10','Jack','Queen','King']
        card_suits = ['Spades','Hearts','Clubs','Diamonds']
        for val in card_vals:
            for suit in card_suits:
                self.cards.append(Card(val, suit))
        print(f'Deck has been built, with {len(self.cards)} cards.')

    def count(self):
        """
        Returns the number of cards in the deck.
        Returns: (int) Number of cards in deck. 
        """
        return len(self.cards)

    def __len__(self):
        """
        Returns the number of cards in the deck.
        Returns: (int) Number of cards in deck. 
        """
        return len(self.cards)

    def show_top(self):
        """
        Shows the bottom card of a deck
        Returns: (str) states the value and suit of the top card.
        """
        return Card.show_card(self.cards[-1])

    def show_bottom(self):
        """
        Shows the bottom card of a deck
        Returns: (str) state the value and suit of the bottom card.
        """
        return Card.show_card(self.cards[0])

    def burn_top(self):
        """
        Discards the top card from the deck.
        """
        burned =  self.cards.pop()
        return burned.show_card()

    def shuffle(self):
        random.shuffle(self.cards)
        return 'Deck has been shuffled.'

    def serve(self, num_cards=1, players = None):
        served = []
        if players:
            for player in players:
                for _ in range(num_cards):
                    player.hand.append(self.cards.pop())
        else:
            for _ in range(num_cards):
                served.append(self.cards.pop())
            return served


class Player(Deck):
    def __init__(self, deck = None):
        self.hand = []
        self.deck = deck

    def draw(self, num_cards=1):
        return self.hand.append(Deck.serve(self.deck, num_cards)[0])

    def discard(self, position=-1): 
        if self.hand and position<len(self.hand):
            self.hand.pop(position)

    def show_hand(self):
        view = []
        for card in self.hand:
            view.append(card.show_card())
        return view

    def count(self):
        return len(self.hand)

    def total(self):
        values = [card.val for card in self.hand]
        for idx, value in enumerate(values):
            if value == 'Jack':
                values[idx] = 11
            elif value == 'Queen':
                values[idx] = 12
            elif value == 'King':
                values[idx] = 13
        return sum(values)

