"""
Deck.py

This module allows you to simulate the behavior of a card. Essentially, this module is a list that allows you to have
a collection of <Card> obj. For convenience several other methods have been built to be able to analyze and study a
deck of cards.
"""


import random

from Card import Card

class Deck(Card):
    """
    Creates the Deck object which builds and contains the 52 cards in a deck of cards. Each of these
    are <Card> objs. 

    Methods:
        build()
        count()
        len()
        show_top()
        show_bottom()
        burn_top()
        shuffle()
        serve()
    
    Returns:
        List of cards as a <Deck> obj
    """
    def __init__(self, cards=[]):
        self.cards = cards
        self.build() # Upon initialization of the object, immediately build the deck of cards.

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
        Returns str representation of the card.
        """
        burned =  self.cards.pop()
        return burned.show_card()

    def shuffle(self):
        """
        Shuffles the cards in deck
        Inputs:
            <Deck> obj
        Returns:
            <Deck> obj which is essentially a list of <Card> obj randomized
            
        """
        'Deck has been shuffled.'
        return random.shuffle(self.cards)

    def serve(self, num_cards=1, players = None):
        """
        Distributes cards to one or more players. 
        Inputs:
            <Deck> obj
            num_cards (int): Number of cards to serve. Default is one. 
            players (list): List of players that cards will be distributed to
        Returns:
            player.hand (list): List of <Card> obj that comprise the hand of a player (for all player)
            or
            served (list): List of <Card> obj that was served for a single player.
        """
        served = []
        if num_cards > len(self.cards): return 'Error! Not enough cards in deck to distribute'
        if players:
            for player in players:
                for _ in range(num_cards):
                    player.hand.append(self.cards.pop())
            return player.hand
        else:
            for _ in range(num_cards):
                served.append(self.cards.pop())
            return served

