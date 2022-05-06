"""
Player.py
Simulates the behaviours of a card player. 
"""


from deck import Deck


class Player(Deck):
    """
    This class allows to simulate the action of a Card Player.

    Inputs: 
        <Deck> obj
    Returns:
        <Player> obj
    """
    def __init__(self, name, deck = None):
        self.hand = []
        self.name = name
        self.deck = deck
        print(f' Player: {name} is ready!')

    def draw(self, num_cards=1):
        """
        Allows player to draw a card from a supplied deck.
        Input:
            num_deck (int): Number of cards to draw from a deck. Default is one.
        Returns: 
            list - A list of <Card> objs.
        
        """
        self.hand += Deck.serve(self.deck, num_cards)
        return self

    def discard(self, position=-1): 
        """
        Allows player to discard a card from their hand. You may optionally enter a position of a card
        for which you want to discard. By default the last card will be discarded.

        Input:
            position (int): Position of card that you wish to discard.
        
        Returns:
            <Card> obj which was discarded.
        """
        if self.hand and position<len(self.hand):
            return self.hand.pop(position)

    def discard_all(self):
        """
        Allows a player to fold their hand of cards.
        Input: 
            <Deck> obj
        Returns:
            None
        """
        self.hand.clear

    def show_hand(self):
        """
        Allows a players to view all cards in their hand. 

        Input:
            <Deck> obj
        Return:
            view (list): List of all the cards (val and suit).
        """
        view = []
        for card in self.hand:
            view.append(card.show_card())
        return view

    def count(self):
        """
        Allows a player to check how many cards they are holding.
        Input:
            <Deck> obj
        Returns:
            (int): Number of cards currently in-hand.
        """
        return len(self.hand)

    def total(self):
        """
        Allows the player to find out the sum of all cards in the hand. 
        Input:
            <Deck>
        Returns:
            (int): Total sum of all values in a supplied hand of cards.
        """
        values = [card.val for card in self.hand]
        for idx, value in enumerate(values):
            if value == 'Jack':
                values[idx] = 11
            elif value == 'Queen':
                values[idx] = 12
            elif value == 'King':
                values[idx] = 13
            else:
                values[idx] = int(value)
        return sum(values)

